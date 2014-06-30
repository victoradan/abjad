# -*- encoding: utf-8 -*-
import os
from abjad import *
import scoremanager
ide = scoremanager.idetools.AbjadIDE(is_test=True)


def test_SegmentPackageManager_interpret_output_ly_01():
    r'''Works when output.ly already exists.
    '''

    ly_path = os.path.join(
        ide._configuration.example_score_packages_directory,
        'red_example_score',
        'segments',
        'segment_01',
        'output.ly',
        )
    pdf_path = os.path.join(
        ide._configuration.example_score_packages_directory,
        'red_example_score',
        'segments',
        'segment_01',
        'output.pdf',
        )

    with systemtools.FilesystemState(keep=[ly_path, pdf_path]):
        os.remove(pdf_path)
        assert not os.path.exists(pdf_path)
        input_ = 'red~example~score g A oli y q'
        ide._run(input_=input_)
        assert os.path.isfile(pdf_path)
        # TODO: make me work again
        #assert systemtools.TestManager.compare_pdfs(
        #    pdf_path, 
        #    pdf_path + '.backup',
        #    )