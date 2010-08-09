from abjad.tools.componenttools._ignore import _ignore
from abjad.tools.componenttools._restore import _restore
from abjad.tools import spannertools
import copy


def clone_components_and_covered_spanners(components, n = 1):
   r'''Clone thread-contiguous `components` together with 
   spanners that cover `components`.

   The steps taken in this function are as follows.
   Withdraw `components` from crossing spanners.
   Preserve spanners that `components` cover.
   Deep copy `components`.
   Reapply crossing spanners to source `components`.
   Return copied components with covered spanners. ::

      abjad> voice = Voice(RigidMeasure((2, 8), leaftools.make_repeated_notes(2)) * 3)
      abjad> pitchtools.set_ascending_diatonic_pitches_on_nontied_pitched_components_in_expr(voice)
      abjad> beam = Beam(voice.leaves[:4])
      abjad> f(voice)
      \new Voice {
              {
                      \time 2/8
                      c'8 [
                      d'8
              }
              {
                      \time 2/8
                      e'8
                      f'8 ]
              }
              {
                      \time 2/8
                      g'8
                      a'8
              }
      }

   ::

      abjad> result = componenttools.clone_components_and_covered_spanners(voice.leaves)
      abjad> result
      (Note(c', 8), Note(d', 8), Note(e', 8), Note(f', 8), Note(g', 8), Note(a', 8))

   ::

      abjad> new_voice = Voice(result)
      abjad> f(new_voice)
      \new Voice {
              c'8 [
              d'8
              e'8
              f'8 ]
              g'8
              a'8
      }

   ::

      abjad> voice.leaves[0] is new_voice.leaves[0]
      False

   ::

      abjad> voice.leaves[0].beam.spanner is new_voice.leaves[0].beam.spanner
      False

   Clone `components` a total of `n` times. ::

      abjad> result = componenttools.clone_components_and_covered_spanners(voice.leaves[:2], n = 3)
      abjad> result
      (Note(c', 8), Note(d', 8), Note(c', 8), Note(d', 8), Note(c', 8), Note(d', 8))

   ::

      abjad> new_voice = Voice(result)
      abjad> f(new_voice)
      \new Voice {
              c'8
              d'8
              c'8
              d'8
              c'8
              d'8
      }

   .. versionchanged:: 1.1.2
      renamed ``clone.covered( )`` to
      ``componenttools.clone_components_and_covered_spanners( )``.
   '''
   from abjad.tools import componenttools
   
   if n < 1:
      return [ ]

   assert componenttools.all_are_thread_contiguous_components(components)

   spanners = spannertools.get_spanners_that_cross_components(components) 
   for spanner in spanners:
      spanner._block_all_components( )

   receipt = _ignore(components)

   result = copy.deepcopy(components)
   for component in result:
      component._update._mark_for_update_to_root( )

   _restore(receipt)

   for spanner in spanners:
      spanner._unblock_all_components( )

   for i in range(n - 1):
      result += clone_components_and_covered_spanners(components)
      
   return result
