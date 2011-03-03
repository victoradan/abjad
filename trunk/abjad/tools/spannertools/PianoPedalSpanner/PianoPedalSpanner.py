from abjad.tools.spannertools.PianoPedalSpanner._PianoPedalSpannerFormatInterface import _PianoPedalSpannerFormatInterface
from abjad.tools.spannertools.Spanner import Spanner


class PianoPedalSpanner(Spanner):
   '''Abjad piano pedal spanner.

   Return piano pedal spanner.
   '''

   def __init__(self, components = None):
      Spanner.__init__(self, components)
      self._format = _PianoPedalSpannerFormatInterface(self)
      self.kind = 'sustain'
      self.style = 'mixed'

   ## PRIVATE ATTRIBUTES ##
   
   _styles = ['text', 'bracket', 'mixed']
         
   _kinds = {'sustain': (r'\sustainOn', r'\sustainOff'), 
              'sostenuto':(r'\sostenutoOn', r'\sostenutoOff'), 
              'corda': (r'\unaCorda', r'\treCorde')}

   ## PUBLIC ATTRIBUTES ##

   @apply
   def kind( ):
      def fget(self):
         return self._kind
      def fset(self, arg):
         if not arg in self._kinds.keys( ):
            raise ValueError("Type must be in %s" % self._kinds.keys( ))
         self._kind = arg
      return property(**locals( ))         

   @apply
   def style( ):
      def fget(self):
         return self._style
      def fset(self, arg):
         if not arg in self._styles:
            raise ValueError("Style must be in %s" % self._styles)
         self._style = arg
      return property(**locals( ))         
