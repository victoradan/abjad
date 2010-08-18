from abjad.tools.pitchtools._leaf_iterables_to_pitch_array import _leaf_iterables_to_pitch_array


def make_empty_pitch_array_from_list_of_pitch_lists(leaf_iterables):
   r'''.. versionadded:: 1.1.2

   Return empty pitch array corresponding to `leaf_iterables`. ::

      abjad> score = Score([ ])
      abjad> score.append(Staff(macros.scale(4)))
      abjad> score.append(Staff(macros.scale(2, Rational(1, 4))))
      abjad> score.append(Staff(tuplettools.FixedDurationTuplet((2, 8), macros.scale(3)) * 2))
      abjad> f(score)
      \new Score <<
              \new Staff {
                      c'8
                      d'8
                      e'8
                      f'8
              }
              \new Staff {
                      c'4
                      d'4
              }
              \new Staff {
                      \times 2/3 {
                              c'8
                              d'8
                              e'8
                      }
                      \times 2/3 {
                              c'8
                              d'8
                              e'8
                      }
              }
      >>

   ::

      abjad> array = pitchtools.make_empty_pitch_array_from_list_of_pitch_lists(score)
      abjad> print array
      [     ] [     ] [     ] [     ]
      [             ] [             ]
      [ ] [     ] [ ] [ ] [     ] [ ]

   .. versionchanged:: 1.1.2
      renamed ``pitchtools.leaf_iterables_to_pitch_array_empty( )`` to
      ``pitchtools.make_empty_pitch_array_from_list_of_pitch_lists( )``.
   '''

#   from abjad.tools import leaftools
#   from abjad.tools import partition
#
#   time_intervals = leaftools.composite_offset_difference_series(leaf_iterables)
#
#   array_width = len(time_intervals)
#   array_depth = len(leaf_iterables)
#
#   pitch_array = PitchArray(array_depth, array_width)
#
#   tokens = notetools.make_quarter_notes_with_lilypond_multipliers([0], time_intervals)
#   for leaf_list, pitch_array_row in zip(leaf_iterables, pitch_array.rows):
#      durations = leaftools.list_prolated_durations_of_leaves_in_expr(leaf_list)
#      parts = componenttools.split_components_once_by_prolated_durations_and_do_not_fracture_crossing_spanners(tokens, durations)
#      part_lengths = [len(part) for part in parts]
#      cells = pitch_array_row.cells
#      grouped_cells = listtools.partition_by_lengths(cells, part_lengths)
#      for group in grouped_cells:
#         pitch_array_row.merge(group)
#
#   return pitch_array

   return _leaf_iterables_to_pitch_array(leaf_iterables, populate = False)
