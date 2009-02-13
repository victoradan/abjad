from abjad import *


def test_clear_leaf_markup_01( ):
   '''Clear multiple pieces of down-markup.'''

   t = FixedDurationTuplet((2, 8), scale(3))
   label_leaf_durations(t)

   r'''
   \times 2/3 {
      c'8 _ \markup { \column { \small 1/8 \small 1/12 } }
      d'8 _ \markup { \column { \small 1/8 \small 1/12 } }
      e'8 _ \markup { \column { \small 1/8 \small 1/12 } }
   }
   '''

   clear_leaf_markup(t)
   
   r'''
   \times 2/3 {
      c'8
      d'8
      e'8
   }
   '''

   assert check(t)
   assert t.format == "\\times 2/3 {\n\tc'8\n\td'8\n\te'8\n}"
