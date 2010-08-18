from abjad import *


def test_VerticalMoment_attack_count_01( ):

   score = Score([ ])
   score.append(Staff([tuplettools.FixedDurationTuplet((4, 8), notetools.make_repeated_notes(3))]))
   piano_staff = scoretools.PianoStaff([ ])
   piano_staff.append(Staff(notetools.make_repeated_notes(2, Rational(1, 4))))
   piano_staff.append(Staff(notetools.make_repeated_notes(4)))
   piano_staff[1].clef.forced = stafftools.Clef('bass')
   score.append(piano_staff)
   macros.diatonicize(list(reversed(score.leaves)))

   r'''
   \new Score <<
           \new Staff {
                   \times 4/3 {
                           d''8
                           c''8
                           b'8
                   }
           }
           \new PianoStaff <<
                   \new Staff {
                           a'4
                           g'4
                   }
                   \new Staff {
                           \clef "bass"
                           f'8
                           e'8
                           d'8
                           c'8
                   }
           >>
   >>
   '''

   vertical_moment = verticalitytools.get_vertical_moment_at_prolated_offset_in_expr(
      score, Rational(0))
   assert vertical_moment.attack_count == 3

   vertical_moment = verticalitytools.get_vertical_moment_at_prolated_offset_in_expr(
      score, Rational(1, 8))
   assert vertical_moment.attack_count == 1
