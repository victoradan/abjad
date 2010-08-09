from abjad import *
import py.test


def test_spannertools_get_spanners_covered_by_components_01( ):
   '''Return unordered set of spanners completely covered
      by the time bounds of thread-contiguous components.'''

   t = Voice(Container(leaftools.make_repeated_notes(2)) * 2)
   pitchtools.set_ascending_diatonic_pitches_on_nontied_pitched_components_in_expr(t)
   beam = Beam(t[0][:])
   slur = Slur(t[1][:])
   trill = Trill(t.leaves)

   r'''
   \new Voice {
           {
                   c'8 [ \startTrillSpan
                   d'8 ]
           }
           {
                   e'8 (
                   f'8 ) \stopTrillSpan
           }
   }
   '''

   spanners = spannertools.get_spanners_covered_by_components([t])
   assert len(spanners) == 3
   assert beam in spanners
   assert slur in spanners
   assert trill in spanners

   spanners = spannertools.get_spanners_covered_by_components(t.leaves)
   assert len(spanners) == 3
   assert beam in spanners
   assert slur in spanners
   assert trill in spanners

   spanners = spannertools.get_spanners_covered_by_components(t[0:1])
   assert len(spanners) == 1
   assert beam in spanners

   spanners = spannertools.get_spanners_covered_by_components(t.leaves[0:1])
   assert spanners == set([ ])
