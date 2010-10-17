from abjad.tools.componenttools.get_proper_parentage_of_component import \
   get_proper_parentage_of_component


def component_to_tuplet_depth(component):
   '''Change `component` to tuplet depth::

      abjad> tuplet = tuplettools.FixedDurationTuplet((2, 8), macros.scale(3))
      abjad> staff = Staff([tuplet])
      abjad> note = staff.leaves[0]

   ::

      abjad> componenttools.component_to_tuplet_depth(note)
      1

   ::

      abjad> componenttools.component_to_tuplet_depth(tuplet)
      0

   ::

      abjad> componenttools.component_to_tuplet_depth(staff)
      0

   Return nonnegative integer.
   '''
   from abjad.components.Tuplet import Tuplet

   result = 0
   for parent in get_proper_parentage_of_component(component):
      if isinstance(parent, Tuplet):
         result += 1
   return result
