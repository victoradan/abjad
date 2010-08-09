from abjad import *


def test_leaftools_get_composite_offset_difference_series_from_leaves_in_expr_01( ):

   staff_1 = Staff([FixedDurationTuplet((4, 8), leaftools.make_repeated_notes(3))])
   staff_2 = Staff(leaftools.make_repeated_notes(4))
   score = Score([staff_1, staff_2])
   pitchtools.set_ascending_diatonic_pitches_on_nontied_pitched_components_in_expr(score)

   r'''
   \new Score <<
           \new Staff {
                   \times 4/3 {
                           c'8
                           d'8
                           e'8
                   }
           }
           \new Staff {
                   f'8
                   g'8
                   a'8
                   b'8
           }
   >>
   '''

   result = leaftools.get_composite_offset_difference_series_from_leaves_in_expr(score)
   assert result == [Rational(1, 8), Rational(1, 24), Rational(1, 12), Rational(1, 12), Rational(1, 24), Rational(1, 8)]
