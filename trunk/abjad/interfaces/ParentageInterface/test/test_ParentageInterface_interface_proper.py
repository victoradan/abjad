from abjad import *


def test_ParentageInterface_interface_proper_01( ):

   tuplet = tuplettools.FixedDurationTuplet((2, 8), macros.scale(3))
   staff = Staff([tuplet])
   note = staff.leaves[0]

   r'''
   \new Staff {
           \times 2/3 {
                   c'8
                   d'8
                   e'8
           }
   }
   '''

   assert len(note.parentage.proper) == 2
   assert note.parentage.proper[0] is tuplet
   assert note.parentage.proper[1] is staff
