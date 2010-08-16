from _create_subdirs_interactive import _create_subdirs_interactive
#from _filter_directories import  _filter_directories
#from _filter_files import _filter_files
from _get_documenting_directories import _get_documenting_directories
from populate_sphinx_directory import populate_sphinx_directory
import os


def build_doc_tree(ABJADPATH, api_doc_path, interactive):
   '''Walk entire Abjad codebase and build corresponding Sphinx doc tree.
   '''

   print 'Building TOC tree ...'
   for documenting_directory in _get_documenting_directories( ):
      documenting_directory = os.path.join(ABJADPATH, documenting_directory)
      #for current_root, directories, files in os.walk(ABJADPATH):
      for current_root, directories, files in os.walk(documenting_directory):
      
         #_filter_directories(directories)
         for directory in directories[:]:
            if directory in ('.svn', 'test'):
               directories.remove(directory)
            elif directory.startswith('_'):
               directories.remove(directory)
         directories.sort( )
      
         #_filter_files(files)
         for file in files[:]:
            if file.startswith('_'):
               files.remove(file)
            elif not file.endswith('.py'):
               files.remove(file)
         files.sort( )

         ## make subdirectories in docs if needed
         abjad_subdir = current_root.split('abjad')[-1].strip(os.path.sep)
         root_dir = os.path.join(api_doc_path, abjad_subdir)
         _create_subdirs_interactive(root_dir, directories, interactive)

         ## populate sphinx directory with sphinx files
         populate_sphinx_directory(root_dir, abjad_subdir, files, interactive)
         #print ''
