from abjad.tools.iterate.get_vertical_moment_at_prolated_offset_in_expr import \
   get_vertical_moment_at_prolated_offset_in_expr as \
   iterate_get_vertical_moment_at_prolated_offset_in_expr


def get_vertical_moment_starting_with_component(expr, governor = None):
   r'''.. versionadded:: 1.1.2

   When `governor` is none, get vertical moment at 
   ``expr.offset.prolated.start`` in ``expr.parentage.root``. ::

      abjad> score = Score([ ])
      abjad> score.append(Staff([FixedDurationTuplet((4, 8), leaftools.make_repeated_notes(3))]))
      abjad> piano_staff = PianoStaff([ ])
      abjad> piano_staff.append(Staff(leaftools.make_repeated_notes(2, Rational(1, 4))))
      abjad> piano_staff.append(Staff(leaftools.make_repeated_notes(4)))
      abjad> piano_staff[1].clef.forced = Clef('bass')
      abjad> score.append(piano_staff)
      abjad> pitchtools.set_ascending_diatonic_pitches_on_nontied_pitched_components_in_expr(list(reversed(score.leaves)))  
      abjad> f(score)
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
      abjad> iterate.get_vertical_moment_starting_with_component(piano_staff[1][1])
      VerticalMoment(Score<<2>>, Staff{1}, {@ 3:4 d''8, c''8, b'8 @}, d''8, PianoStaff<<2>>, Staff{2}, a'4, Staff{4}, e'8)

   When `governor` is not none, get vertical moment at
   ``expr.offset.prolated.start`` in `governor`. ::

      abjad> iterate.get_vertical_moment_starting_with_component(piano_staff[1][1], piano_staff)
      VerticalMoment(PianoStaff<<2>>, Staff{2}, a'4, Staff{4}, e'8)

   .. todo:: optimize without full-component traversal.

   .. versionchanged:: 1.1.2
      renamed ``iterate.get_vertical_moment_starting_with( )`` to
      ``iterate.get_vertical_moment_starting_with_component( )``.
   '''

   prolated_offset = expr.offset.prolated.start

   if governor is None:
      governor = expr.parentage.root

   return iterate_get_vertical_moment_at_prolated_offset_in_expr(
      governor, prolated_offset)
