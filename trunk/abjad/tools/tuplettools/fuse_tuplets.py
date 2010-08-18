from abjad.components.Container import Container
from abjad.exceptions import TupletFuseError
from abjad.core import Rational
from abjad.components._Tuplet import _Tuplet
from abjad.tools.tuplettools.FixedDurationTuplet import FixedDurationTuplet
from abjad.components._Tuplet import FixedMultiplierTuplet


def fuse_tuplets(tuplets):
   r'''Fuse parent-contiguous `tuplets`::

      abjad> t1 = tuplettools.FixedDurationTuplet((2, 8), macros.scale(3))
      abjad> spannertools.BeamSpanner(t1[:])
      abjad> t2 = tuplettools.FixedDurationTuplet((2, 16), macros.scale(3, Rational(1, 16)))
      abjad> spannertools.SlurSpanner(t2[:])
      abjad> staff = Staff([t1, t2])
      abjad> f(staff)
      \new Staff {
         \times 2/3 {
            c'8 [
            d'8
            e'8 ]
         }
         \times 2/3 {
            c'16 (
            d'16
            e'16 )
         }
      }
      
   ::
      
      abjad> tuplettools.fuse_tuplets(staff[:])
      FixedDurationTuplet(3/8, [c'8, d'8, e'8, c'16, d'16, e'16])

   ::

      abjad> f(staff)
      \new Staff {
         \times 2/3 {
            c'8 [
            d'8
            e'8 ]
            c'16 (
            d'16
            e'16 )
         }
      }

   Return new tuplet.

   Fuse zero or more parent-contiguous `tuplets`.

   Allow in-score `tuplets`.

   Allow outside-of-score `tuplets`.

   All `tuplets` must carry the same multiplier.

   All `tuplets` must be of the same type.

   .. versionchanged:: 1.1.2
      renamed ``fuse.tuplets_by_reference( )`` to
      ``tuplettools.fuse_tuplets( )``.
   '''

   from abjad.tools import componenttools
   from abjad.tools import containertools
   from abjad.tools import scoretools

   assert componenttools.all_are_contiguous_components_in_same_parent(tuplets,
      klasses = (_Tuplet))

   if len(tuplets) == 0:
      return None

   first = tuplets[0]
   first_multiplier = first.duration.multiplier
   first_type = type(first)
   for tuplet in tuplets[1:]:
      if tuplet.duration.multiplier != first_multiplier:
         raise TupletFuseError('tuplets must carry same multiplier.')
      if type(tuplet) != first_type:
         raise TupletFuseError('tuplets must be same type.')

   if isinstance(first, FixedDurationTuplet):
      total_contents_duration = sum([x.duration.contents for x in tuplets])
      new_target_duration = first_multiplier * total_contents_duration
      new_tuplet = FixedDurationTuplet(new_target_duration, [ ])
   elif isinstance(first, FixedMultiplierTuplet):
      new_tuplet = FixedMultiplierTuplet(first_multiplier, [ ])
   else:
      raise TypeError('unknown tuplet type.')

   wrapped = False
   if tuplets[0].parentage.root is not tuplets[-1].parentage.root:
      dummy_container = Container(tuplets) 
      wrapped = True
   containertools.move_parentage_children_and_spanners_from_components_to_empty_container(tuplets, new_tuplet)

   if wrapped:
      containertools.delete_contents_of_container(dummy_container)
   
   return new_tuplet
