import os
from xml.etree import ElementTree


def _import_test_file( ):
   f = open(os.path.join(os.path.dirname(__file__), 'test', 'SchbAvMaSample.xml'), 'r')
   r = ElementTree.parse(f).getroot( )
   f.close( )
   return r

