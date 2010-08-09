from abjad import *
import py.test


def test_iterate_get_measure_number_in_expr_01( ):

   t = Staff(RigidMeasure((2, 8), leaftools.make_repeated_notes(2)) * 3)
   pitchtools.set_ascending_diatonic_pitches_on_nontied_pitched_components_in_expr(t)

   assert iterate.get_measure_number_in_expr(t, 1) is t[0]
   assert iterate.get_measure_number_in_expr(t, 2) is t[1]
   assert iterate.get_measure_number_in_expr(t, 3) is t[2]



def test_iterate_get_measure_number_in_expr_02( ):

   t = Staff(RigidMeasure((2, 8), leaftools.make_repeated_notes(2)) * 3)
   pitchtools.set_ascending_diatonic_pitches_on_nontied_pitched_components_in_expr(t)

   assert py.test.raises(ValueError, 'iterate.get_measure_number_in_expr(t, -1)')
