from abjad.tools import *
from experimental.abjadbooktools.CodeBlock import CodeBlock
from experimental.abjadbooktools.OutputFormat import OutputFormat
import os
import shutil
import tempfile


class AbjadBookProcessor(abctools.AbjadObject):

    ### CLASS ATTRIBUTES ###

    __slots__ = ('_lines', '_output_format', '_skip_rendering')

    ### INITIALIZER ###

    def __init__(self, lines, output_format, skip_rendering=False):
        assert isinstance(output_format, OutputFormat)
        self._lines = tuple(lines)
        self._output_format = output_format
        self._skip_rendering = bool(skip_rendering)

    ### SPECIAL METHOD ###

    def __call__(self, directory):

        directory = os.path.abspath(directory)

        # Verify input, and extract code blocks
        code_blocks = self._extract_code_blocks(self.lines)        

        # Create a temporary directory, and step into it.
        tmp_directory = self._setup_tmp_directory(directory)
        os.chdir(tmp_directory)

        # Process code blocks, and render images inside the temporary directory
        pipe = self._setup_pipe()
        image_count = self._process_code_blocks(pipe, code_blocks, tmp_directory)
        ly_filenames = self._extract_ly_filenames(code_blocks)
        self._cleanup_pipe(pipe)
        if not self.skip_rendering:
            self._render_ly_files(ly_filenames, self.output_format)

        # Step out of the tmp directory, back to the original, and cleanup.
        os.chdir(directory)
        self._cleanup_image_files(directory, tmp_directory, image_count)
        self._cleanup_tmp_directory(tmp_directory)

        # Interleave newly reformatted code with the old, and return.
        return self._interleave_source_with_code_blocks(self.lines, code_blocks, self.output_format)

    ### PUBLIC READ-ONLY PROPERTIES ###

    @property
    def lines(self):
        return self._lines

    @property
    def output_format(self):
        return self._output_format

    @property
    def skip_rendering(self):
        return self._skip_rendering

    ### PRIVATE METHODS ###

    def _cleanup_image_files(self, directory, tmp_directory, image_count):
        image_directory = os.path.join(directory, 'images')
        if not os.path.isdir(image_directory):
            os.mkdir(image_directory)
        for x in os.listdir(image_directory):
            if x.startswith('image-'):
                number = int(x.partition('.')[0][6:])
                if image_count < number:
                    os.remove(x)
        for x in os.listdir(tmp_directory):
            if x.endswith(('.pdf', '.png')):
                old = os.path.join(tmp_directory, x)
                new = os.path.join(image_directory, x)
                os.rename(old, new)

    def _cleanup_pipe(self, pipe):
        pipe.write('quit()\n')
        pipe.close()

    def _cleanup_tmp_directory(self, tmp_directory):
        shutil.rmtree(tmp_directory)

    def _extract_code_blocks(self, lines):
        blocks = []
        block = []
        starting_line_number = 0
        in_block = False
        for i, line in enumerate(lines):
            if line.startswith('<abjad>'):
                if in_block:
                    raise Exception('Extra opening tag at line {}.'.format(i))
                else:
                    in_block = True
                    block = [line]
                    starting_line_number = i
            elif line.startswith('</abjad>'):
                if in_block:
                    in_block = False
                    hide = 'hide=true' in block[0]
                    strip_prompt = 'strip_prompt=true' in block[0]
                    code_block = CodeBlock(block[1:],
                        starting_line_number,
                        i,
                        hide=hide,
                        strip_prompt=strip_prompt)
                    blocks.append(code_block)
                else:
                    raise Exception('Extra closing tag at line {}'.format(i))
            elif in_block:
                block.append(line)
        if in_block:
            raise Exception('Unterminated tag at EOF.')
        return tuple(blocks)

    def _extract_ly_filenames(self, code_blocks):
        filenames = []
        for code_block in code_blocks:
            for result in code_block.processed_results:
                if isinstance(result, str):
                    filenames.append(result)
        return filenames

    def _interleave_source_with_code_blocks(self, lines, code_blocks, output_format):
        interleaved = []
        interleaved.append('\n'.join(lines[:code_blocks[0].starting_line_number]))
        for pair in sequencetools.iterate_sequence_pairwise_strict(code_blocks):
            first_block, second_block = pair
            interleaved.extend(output_format(first_block))
            interleaved.append('\n'.join(lines[first_block.ending_line_number + 1:second_block.starting_line_number]))
        interleaved.extend(output_format(code_blocks[-1]))
        interleaved.append('\n'.join(lines[code_blocks[-1].ending_line_number + 1:]))
        return '\n'.join(interleaved)

    def _process_code_blocks(self, pipe, code_blocks, directory):
        image_count = 0
        for code_block in code_blocks:
            image_count = code_block(pipe, image_count, directory)
        return image_count

    def _setup_pipe(self):
        pipe = documentationtools.Pipe()
        pipe.read_wait()
        pipe.write('from abjad import *\n')
        pipe.read_wait()
        return pipe

    def _setup_tmp_directory(self, directory):
        tmp_directory = os.path.abspath(tempfile.mkdtemp(dir=directory))
        return tmp_directory

    def _render_ly_files(self, filenames, output_format):
        if output_format.image_format == 'png':
            for filename in filenames:
                self._render_png_image(filename)
        elif output_format.image_format == 'pdf':
            for filename in filenames:
                self._render_pdf_image(filename)
            
    def _render_pdf_image(self, filename):
        iotools.spawn_subprocess('lilypond {}.ly'.format(filename))
        iotools.spawn_subprocess('pdfcrop {}.pdf {}.pdf'.format(filename, filename))

    def _render_png_image(self, filename):
        iotools.spawn_subprocess('lilypond --png -dresolution=300 {}.ly'.format(filename))
        iotools.spawn_subprocess('convert {}.png -trim -resample 40%% {}.png'.format(filename, filename))

