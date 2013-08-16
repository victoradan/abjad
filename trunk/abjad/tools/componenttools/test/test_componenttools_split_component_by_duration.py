# -*- encoding: utf-8 -*-
from abjad import *


def test_componenttools_split_component_by_duration_01():

    staff = Staff()
    staff.append(Measure((2, 8), "c'8 d'8"))
    staff.append(Measure((2, 8), "e'8 f'8"))
    spannertools.BeamSpanner(staff[0])
    spannertools.BeamSpanner(staff[1])
    spannertools.SlurSpanner(staff.select_leaves())

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 2/8
                c'8 [ (
                d'8 ]
            }
            {
                e'8 [
                f'8 ] )
            }
        }
        '''
        )

    halves = componenttools.split_component_by_duration(
        staff.select_leaves()[0], 
        Duration(1, 32), 
        fracture_spanners=False, 
        tie_split_notes=False,
        )

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 2/8
                c'32 [ (
                c'16.
                d'8 ]
            }
            {
                e'8 [
                f'8 ] )
            }
        }
        '''
        )

    assert select(staff).is_well_formed()
    assert isinstance(halves, tuple)
    assert isinstance(halves[0], list)
    assert isinstance(halves[1], list)


def test_componenttools_split_component_by_duration_02():

    staff = Staff()
    staff.append(Measure((2, 8), "c'8 d'8"))
    staff.append(Measure((2, 8), "e'8 f'8"))
    spannertools.BeamSpanner(staff[0])
    spannertools.BeamSpanner(staff[1])
    spannertools.SlurSpanner(staff.select_leaves())

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 2/8
                c'8 [ (
                d'8 ]
            }
            {
                e'8 [
                f'8 ] )
            }
        }
        '''
        )

    halves = componenttools.split_component_by_duration(
        staff[0], 
        Duration(1, 32), 
        fracture_spanners=False, 
        tie_split_notes=False,
        )

    r'''
    \new Staff {
        {
            \time 1/32
            c'32 [ (
        }
        {
            \time 7/32
            c'16.
            d'8 ]
        }
        {
            \time 2/8
            e'8 [
            f'8 ] )
        }
    }
    '''

    assert select(staff).is_well_formed()
    assert isinstance(halves, tuple)
    assert isinstance(halves[0], list)
    assert isinstance(halves[1], list)
    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 1/32
                c'32 [ (
            }
            {
                \time 7/32
                c'16.
                d'8 ]
            }
            {
                \time 2/8
                e'8 [
                f'8 ] )
            }
        }
        '''
        )


def test_componenttools_split_component_by_duration_03():

    staff = Staff()
    staff.append(Measure((2, 8), "c'8 d'8"))
    staff.append(Measure((2, 8), "e'8 f'8"))
    spannertools.BeamSpanner(staff[0])
    spannertools.BeamSpanner(staff[1])
    spannertools.SlurSpanner(staff.select_leaves())

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 2/8
                c'8 [ (
                d'8 ]
            }
            {
                e'8 [
                f'8 ] )
            }
        }
        '''
        )

    halves = componenttools.split_component_by_duration(
        staff, 
        Duration(1, 32), 
        fracture_spanners=False, 
        tie_split_notes=False,
        )

    "halves[0][0]"

    r'''
    \new Staff {
        {
            \time 1/32
            c'32 [ (
        }
    }
    '''

    assert testtools.compare(
        halves[0][0],
        r'''
        \new Staff {
            {
                \time 1/32
                c'32 [ (
            }
        }
        '''
        )

    "halves[1][0]"

    r'''
    \new Staff {
        {
            \time 7/32
            c'16.
            d'8 ]
        }
        {
            \time 2/8
            e'8 [
            f'8 ] )
        }
    }
    '''

    assert testtools.compare(
        halves[1][0],
        r'''
        \new Staff {
            {
                \time 7/32
                c'16.
                d'8 ]
            }
            {
                \time 2/8
                e'8 [
                f'8 ] )
            }
        }
        '''
        )


def test_componenttools_split_component_by_duration_04():
    r'''Split one leaf in score.
    Do not fracture spanners. But do tie after split.
    '''

    staff = Staff()
    staff.append(Measure((2, 8), "c'8 d'8"))
    staff.append(Measure((2, 8), "e'8 f'8"))
    spannertools.BeamSpanner(staff[0])
    spannertools.BeamSpanner(staff[1])
    spannertools.SlurSpanner(staff.select_leaves())

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 2/8
                c'8 [ (
                d'8 ]
            }
            {
                e'8 [
                f'8 ] )
            }
        }
        '''
        )

    halves = componenttools.split_component_by_duration(
        staff.select_leaves()[0], 
        Duration(1, 32), 
        fracture_spanners=False, 
        tie_split_notes=True,
        )

    r'''
    \new Staff {
        {
            \time 2/8
            c'32 [ ( ~
            c'16.
            d'8 ]
        }
        {
            \time 2/8
            e'8 [
            f'8 ] )
        }
    }
    '''

    assert select(staff).is_well_formed()
    assert isinstance(halves, tuple)
    assert isinstance(halves[0], list)
    assert isinstance(halves[1], list)
    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 2/8
                c'32 [ ( ~
                c'16.
                d'8 ]
            }
            {
                e'8 [
                f'8 ] )
            }
        }
        '''
        )


def test_componenttools_split_component_by_duration_05():
    r'''Split one measure in score.
    Do not fracture spanners. But do add tie after split.
    '''

    staff = Staff()
    staff.append(Measure((2, 8), "c'8 d'8"))
    staff.append(Measure((2, 8), "e'8 f'8"))
    spannertools.BeamSpanner(staff[0])
    spannertools.BeamSpanner(staff[1])
    spannertools.SlurSpanner(staff.select_leaves())

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 2/8
                c'8 [ (
                d'8 ]
            }
            {
                e'8 [
                f'8 ] )
            }
        }
        '''
        )

    halves = componenttools.split_component_by_duration(
        staff[0], 
        Duration(1, 32), 
        fracture_spanners=False, 
        tie_split_notes=True,
        )

    r'''
    \new Staff {
        {
            \time 1/32
            c'32 [ ( ~
        }
        {
            \time 7/32
            c'16.
            d'8 ]
        }
        {
            \time 2/8
            e'8 [
            f'8 ] )
        }
    }
    '''

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 1/32
                c'32 [ ( ~
            }
            {
                \time 7/32
                c'16.
                d'8 ]
            }
            {
                \time 2/8
                e'8 [
                f'8 ] )
            }
        }
        '''
        )

    assert select(staff).is_well_formed()
    assert isinstance(halves, tuple)
    assert isinstance(halves[0], list)
    assert isinstance(halves[1], list)


def test_componenttools_split_component_by_duration_06():
    r'''Split in-score measure with power-of-two time signature denominator
    at split offset without power-of-two denominator.
    Do not fracture spanners and do not tie leaves after split.
    '''

    staff = Staff()
    staff.append(Measure((2, 8), "c'8 d'8"))
    staff.append(Measure((2, 8), "e'8 f'8"))
    spannertools.BeamSpanner(staff[0])
    spannertools.BeamSpanner(staff[1])
    spannertools.SlurSpanner(staff.select_leaves())

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 2/8
                c'8 [ (
                d'8 ]
            }
            {
                e'8 [
                f'8 ] )
            }
        }
        '''
        )

    halves = componenttools.split_component_by_duration(
        staff[0], 
        Duration(1, 5), 
        fracture_spanners=False,
        )

    # TODO: The tie at the split locus here is a (small) bug.
    #       Eventually should fix.
    #       The tie after the d'16. is the incorrect one.
    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 4/20
                \scaleDurations #'(4 . 5) {
                    c'8 [ ( ~
                    c'32
                    d'16. ~
                }
            }
            {
                \time 1/20
                \scaleDurations #'(4 . 5) {
                    d'16 ]
                }
            }
            {
                \time 2/8
                e'8 [
                f'8 ] )
            }
        }
        '''
        )

    assert select(staff).is_well_formed()
    assert len(halves) == 2


def test_componenttools_split_component_by_duration_07():
    r'''Split in-score measure with power-of-two time signature denominator
    at split offset without power-of-two denominator.
    Do fracture spanners and do tie leaves after split.
    '''

    staff = Staff()
    staff.append(Measure((2, 8), "c'8 d'8"))
    staff.append(Measure((2, 8), "e'8 f'8"))
    spannertools.BeamSpanner(staff[0])
    spannertools.BeamSpanner(staff[1])
    spannertools.SlurSpanner(staff.select_leaves())

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 2/8
                c'8 [ (
                d'8 ]
            }
            {
                e'8 [
                f'8 ] )
            }
        }
        '''
        )

    halves = componenttools.split_component_by_duration(
        staff[0], 
        Duration(1, 5), 
        fracture_spanners=False, 
        tie_split_notes=True,
        )

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 4/20
                \scaleDurations #'(4 . 5) {
                    c'8 [ ( ~
                    c'32
                    d'16. ~
                }
            }
            {
                \time 1/20
                \scaleDurations #'(4 . 5) {
                    d'16 ]
                }
            }
            {
                \time 2/8
                e'8 [
                f'8 ] )
            }
        }
        '''
        )

    assert select(staff).is_well_formed()
    assert len(halves) == 2


def test_componenttools_split_component_by_duration_08():
    r'''Split leaf in score and fracture spanners.
    '''

    staff = Staff()
    staff.append(Measure((2, 8), "c'8 d'8"))
    staff.append(Measure((2, 8), "e'8 f'8"))
    spannertools.BeamSpanner(staff[0])
    spannertools.BeamSpanner(staff[1])
    spannertools.SlurSpanner(staff.select_leaves())

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 2/8
                c'8 [ (
                d'8 ]
            }
            {
                e'8 [
                f'8 ] )
            }
        }
        '''
        )

    halves = componenttools.split_component_by_duration(
        staff.select_leaves()[0], 
        Duration(1, 32), 
        fracture_spanners=True, 
        tie_split_notes=False,
        )

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 2/8
                c'32 [ ( )
                c'16. (
                d'8 ]
            }
            {
                e'8 [
                f'8 ] )
            }
        }
        '''
        )

    assert select(staff).is_well_formed()
    assert len(halves) == 2
    assert isinstance(halves, tuple)
    assert isinstance(halves[0], list)
    assert isinstance(halves[1], list)


def test_componenttools_split_component_by_duration_09():
    r'''Split measure in score and fracture spanners.
    '''

    staff = Staff()
    staff.append(Measure((2, 8), "c'8 d'8"))
    staff.append(Measure((2, 8), "e'8 f'8"))
    spannertools.BeamSpanner(staff[0])
    spannertools.BeamSpanner(staff[1])
    spannertools.SlurSpanner(staff.select_leaves())

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 2/8
                c'8 [ (
                d'8 ]
            }
            {
                e'8 [
                f'8 ] )
            }
        }
        '''
        )

    halves = componenttools.split_component_by_duration(
        staff[0], 
        Duration(1, 32), 
        fracture_spanners=True, 
        tie_split_notes=False,
        )

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 1/32
                c'32 [ ] ( )
            }
            {
                \time 7/32
                c'16. [ (
                d'8 ]
            }
            {
                \time 2/8
                e'8 [
                f'8 ] )
            }
        }
        '''
        )

    assert select(staff).is_well_formed()
    assert isinstance(halves, tuple)
    assert isinstance(halves[0], list)
    assert isinstance(halves[1], list)


def test_componenttools_split_component_by_duration_10():
    r'''Split staff outside of score and fracture spanners.
    '''

    staff = Staff()
    staff.append(Measure((2, 8), "c'8 d'8"))
    staff.append(Measure((2, 8), "e'8 f'8"))
    spannertools.BeamSpanner(staff[0])
    spannertools.BeamSpanner(staff[1])
    spannertools.SlurSpanner(staff.select_leaves())

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 2/8
                c'8 [ (
                d'8 ]
            }
            {
                e'8 [
                f'8 ] )
            }
        }
        '''
        )

    halves = componenttools.split_component_by_duration(
        staff, 
        Duration(1, 32), 
        fracture_spanners=True, 
        tie_split_notes=False,
        )

    assert testtools.compare(
        halves[0][0],
        r'''
        \new Staff {
            {
                \time 1/32
                c'32 [ ] ( )
            }
        }
        '''
        )

    assert testtools.compare(
        halves[1][0],
        r'''
        \new Staff {
            {
                \time 7/32
                c'16. [ (
                d'8 ]
            }
            {
                \time 2/8
                e'8 [
                f'8 ] )
            }
        }
        '''
        )


def test_componenttools_split_component_by_duration_11():
    r'''Split leaf in score at nonzero index.
    Fracture spanners.
    Test comes from a bug fix.
    '''

    staff = Staff()
    staff.append(Measure((2, 8), "c'8 d'8"))
    staff.append(Measure((2, 8), "e'8 f'8"))
    spannertools.BeamSpanner(staff[0])
    spannertools.BeamSpanner(staff[1])
    spannertools.SlurSpanner(staff.select_leaves())

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 2/8
                c'8 [ (
                d'8 ]
            }
            {
                e'8 [
                f'8 ] )
            }
        }
        '''
        )

    componenttools.split_component_by_duration(
        staff.select_leaves()[1], 
        Duration(1, 32), 
        fracture_spanners=True, 
        tie_split_notes=False,
        )

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 2/8
                c'8 [ (
                d'32 )
                d'16. ] (
            }
            {
                e'8 [
                f'8 ] )
            }
        }
        '''
        )

    assert select(staff).is_well_formed()


def test_componenttools_split_component_by_duration_12():
    r'''Split container over leaf at nonzero index.
    Fracture spanners.
    Test results from bug fix.
    '''

    staff = Staff()
    staff.append(Measure((2, 8), "c'8 d'8"))
    staff.append(Measure((2, 8), "e'8 f'8"))
    spannertools.BeamSpanner(staff[0])
    spannertools.BeamSpanner(staff[1])
    spannertools.SlurSpanner(staff.select_leaves())

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 2/8
                c'8 [ (
                d'8 ]
            }
            {
                e'8 [
                f'8 ] )
            }
        }
        '''
        )

    componenttools.split_component_by_duration(
        staff[0], 
        Duration(7, 32), 
        fracture_spanners=True, 
        tie_split_notes=False,
        )

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 7/32
                c'8 [ (
                d'16. ] )
            }
            {
                \time 1/32
                d'32 [ ] (
            }
            {
                \time 2/8
                e'8 [
                f'8 ] )
            }
        }
        '''
        )

    assert select(staff).is_well_formed()


def test_componenttools_split_component_by_duration_13():
    r'''Split container between leaves and fracture spanners.
    '''

    staff = Staff()
    staff.append(Measure((2, 8), "c'8 d'8"))
    staff.append(Measure((2, 8), "e'8 f'8"))
    spannertools.BeamSpanner(staff[0])
    spannertools.BeamSpanner(staff[1])
    spannertools.SlurSpanner(staff.select_leaves())

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 2/8
                c'8 [ (
                d'8 ]
            }
            {
                e'8 [
                f'8 ] )
            }
        }
        '''
        )

    parts = componenttools.split_component_by_duration(
        staff[0], 
        Duration(1, 8), 
        fracture_spanners=True,
        )

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 1/8
                c'8 [ ] ( )
            }
            {
                d'8 [ ] (
            }
            {
                \time 2/8
                e'8 [
                f'8 ] )
            }
        }
        '''
        )

    assert select(staff).is_well_formed()
    assert isinstance(parts, tuple)
    assert isinstance(parts[0], list)
    assert isinstance(parts[1], list)


def test_componenttools_split_component_by_duration_14():
    r'''Split leaf outside of score and fracture spanners.
    '''

    note = Note(0, (1, 8))
    spannertools.BeamSpanner(note)

    assert note.lilypond_format == "c'8 [ ]"

    halves = componenttools.split_component_by_duration(
        note, 
        Duration(1, 32), 
        fracture_spanners=True,
        )

    assert halves[0][0].lilypond_format == "c'32 [ ] ~"
    assert select(halves[0][0]).is_well_formed()

    assert halves[1][0].lilypond_format == "c'16. [ ]"
    assert select(halves[1][0]).is_well_formed()


def test_componenttools_split_component_by_duration_15():
    r'''Split leaf in score and fracture spanners.
    Tie leaves after split.
    '''

    staff = Staff()
    staff.append(Measure((2, 8), "c'8 d'8"))
    staff.append(Measure((2, 8), "e'8 f'8"))
    spannertools.BeamSpanner(staff[0])
    spannertools.BeamSpanner(staff[1])
    spannertools.SlurSpanner(staff.select_leaves())

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 2/8
                c'8 [ (
                d'8 ]
            }
            {
                e'8 [
                f'8 ] )
            }
        }
        '''
        )

    halves = componenttools.split_component_by_duration(
        staff.select_leaves()[0], 
        Duration(1, 32), 
        fracture_spanners=True, 
        tie_split_notes=True,
        )

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 2/8
                c'32 [ ( ) ~
                c'16. (
                d'8 ]
            }
            {
                e'8 [
                f'8 ] )
            }
        }
        '''
        )

    assert select(staff).is_well_formed()
    assert len(halves) == 2
    assert isinstance(halves, tuple)
    assert isinstance(halves[0], list)
    assert isinstance(halves[1], list)


def test_componenttools_split_component_by_duration_16():
    r'''Split measure in score and fracture spanners.
    Tie leaves after split.
    '''

    staff = Staff()
    staff.append(Measure((2, 8), "c'8 d'8"))
    staff.append(Measure((2, 8), "e'8 f'8"))
    spannertools.BeamSpanner(staff[0])
    spannertools.BeamSpanner(staff[1])
    spannertools.SlurSpanner(staff.select_leaves())

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 2/8
                c'8 [ (
                d'8 ]
            }
            {
                e'8 [
                f'8 ] )
            }
        }
        '''
        )

    halves = componenttools.split_component_by_duration(
        staff[0], 
        Duration(1, 32), 
        fracture_spanners=True, 
        tie_split_notes=True,
        )

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 1/32
                c'32 [ ] ( ) ~
            }
            {
                \time 7/32
                c'16. [ (
                d'8 ]
            }
            {
                \time 2/8
                e'8 [
                f'8 ] )
            }
        }
        '''
        )

    assert select(staff).is_well_formed()
    assert isinstance(halves, tuple)
    assert isinstance(halves[0], list)
    assert isinstance(halves[1], list)


def test_componenttools_split_component_by_duration_17():
    r'''Split in-score measure with power-of-two time signature denominator
    at split offset without power-of-two denominator.
    Do fracture spanners but do not tie leaves after split.
    '''

    staff = Staff()
    staff.append(Measure((2, 8), "c'8 d'8"))
    staff.append(Measure((2, 8), "e'8 f'8"))
    spannertools.BeamSpanner(staff[0])
    spannertools.BeamSpanner(staff[1])
    spannertools.SlurSpanner(staff.select_leaves())

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 2/8
                c'8 [ (
                d'8 ]
            }
            {
                e'8 [
                f'8 ] )
            }
        }
        '''
        )

    halves = componenttools.split_component_by_duration(
        staff[0], 
        Duration(1, 5), 
        fracture_spanners=True, 
        tie_split_notes=False,
        )

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 4/20
                \scaleDurations #'(4 . 5) {
                    c'8 [ ( ~
                    c'32
                    d'16. ] )
                }
            }
            {
                \time 1/20
                \scaleDurations #'(4 . 5) {
                    d'16 [ ] (
                }
            }
            {
                \time 2/8
                e'8 [
                f'8 ] )
            }
        }
        '''
        )

    assert select(staff).is_well_formed()
    assert len(halves) == 2


def test_componenttools_split_component_by_duration_18():
    r'''Split in-score measure with power-of-two time signature denominator at
    split offset without power-of-two denominator.
    Do fracture spanners and do tie leaves after split.
    '''

    staff = Staff()
    staff.append(Measure((2, 8), "c'8 d'8"))
    staff.append(Measure((2, 8), "e'8 f'8"))
    spannertools.BeamSpanner(staff[0])
    spannertools.BeamSpanner(staff[1])
    spannertools.SlurSpanner(staff.select_leaves())

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 2/8
                c'8 [ (
                d'8 ]
            }
            {
                e'8 [
                f'8 ] )
            }
        }
        '''
        )

    halves = componenttools.split_component_by_duration(
        staff[0], 
        Duration(1, 5), 
        fracture_spanners=True, 
        tie_split_notes=True,
        )

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 4/20
                \scaleDurations #'(4 . 5) {
                    c'8 [ ( ~
                    c'32
                    d'16. ] ) ~
                }
            }
            {
                \time 1/20
                \scaleDurations #'(4 . 5) {
                    d'16 [ ] (
                }
            }
            {
                \time 2/8
                e'8 [
                f'8 ] )
            }
        }
        '''
        )

    assert select(staff).is_well_formed()
    assert len(halves) == 2


def test_componenttools_split_component_by_duration_19():
    r'''Split measure with power-of-two time signature denominator at
    split offset without power-of-two denominator.
    Do fracture spanners but do not tie across split locus.
    This test results from a fix.
    What's being tested here is contents rederivation.
    '''

    staff = Staff()
    staff.append(Measure((3, 8), "c'8 d'8 e'8"))
    staff.append(Measure((3, 8), "c'8 d'8 e'8"))
    spannertools.BeamSpanner(staff[0])
    spannertools.BeamSpanner(staff[1])
    spannertools.SlurSpanner(staff.select_leaves())

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 3/8
                c'8 [ (
                d'8
                e'8 ]
            }
            {
                c'8 [
                d'8
                e'8 ] )
            }
        }
        '''
        )

    halves = componenttools.split_component_by_duration(
        staff[0], 
        Duration(7, 20), 
        fracture_spanners=True,
        )

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 14/40
                \scaleDurations #'(4 . 5) {
                    c'8 [ ( ~
                    c'32
                    d'8 ~
                    d'32
                    e'8 ] )
                }
            }
            {
                \time 1/40
                \scaleDurations #'(4 . 5) {
                    e'32 [ ] (
                }
            }
            {
                \time 3/8
                c'8 [
                d'8
                e'8 ] )
            }
        }
        '''
        )

    assert select(staff).is_well_formed()
    assert len(halves) == 2


def test_componenttools_split_component_by_duration_20():
    r'''Split leaf with LilyPond multiplier.
    Split at split offset with power-of-two denominator.
    Halves carry original written duration.
    Halves carry adjusted LilyPond multipliers.
    '''

    note = Note(0, (1, 8))
    note.lilypond_duration_multiplier = Fraction(1, 2)

    assert note.lilypond_format == "c'8 * 1/2"

    halves = componenttools.split_component_by_duration(
        note, 
        Duration(1, 32), 
        fracture_spanners=True, 
        tie_split_notes=False,
        )

    assert halves[0][0].lilypond_format == "c'8 * 1/4"
    assert halves[1][0].lilypond_format == "c'8 * 1/4"

    assert len(halves) == 2
    assert select(halves[0][0]).is_well_formed()
    assert select(halves[1][0]).is_well_formed()


def test_componenttools_split_component_by_duration_21():
    r'''Split leaf with LilyPond multiplier.
    Split at offset without power-of-two denominator.
    Halves carry original written duration.
    Halves carry adjusted LilyPond multipliers.
    '''

    note = Note(0, (1, 8))
    note.lilypond_duration_multiplier = Fraction(1, 2)

    assert note.lilypond_format == "c'8 * 1/2"

    halves = componenttools.split_component_by_duration(
        note, 
        Duration(1, 48), 
        fracture_spanners=True, 
        tie_split_notes=False,
        )

    assert halves[0][0].lilypond_format == "c'8 * 1/6"
    assert halves[1][0].lilypond_format == "c'8 * 1/3"

    assert len(halves) == 2
    assert select(halves[0][0]).is_well_formed()
    assert select(halves[1][0]).is_well_formed()


def test_componenttools_split_component_by_duration_22():
    r'''Split measure with power-of-two time signature denominator 
    with multiplied leaes. Split at between-leaf offset with 
    power-of-two denominator. Leaves remain unaltered.
    '''

    staff = Staff()
    staff.append(Measure((2, 16), "c'8 d'8"))
    staff.append(Measure((2, 16), "e'8 f'8"))
    for leaf in staff.select_leaves():
        leaf.lilypond_duration_multiplier = Fraction(1, 2)
    spannertools.BeamSpanner(staff[0])
    spannertools.BeamSpanner(staff[1])
    spannertools.SlurSpanner(staff.select_leaves())

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 2/16
                c'8 * 1/2 [ (
                d'8 * 1/2 ]
            }
            {
                e'8 * 1/2 [
                f'8 * 1/2 ] )
            }
        }
        '''
        )

    halves = componenttools.split_component_by_duration(
        staff[0], 
        Duration(1, 16), 
        fracture_spanners=True,
        )

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 1/16
                c'8 * 1/2 [ ] ( )
            }
            {
                d'8 * 1/2 [ ] (
            }
            {
                \time 2/16
                e'8 * 1/2 [
                f'8 * 1/2 ] )
            }
        }
        '''
        )

    assert select(staff).is_well_formed()
    assert len(halves) == 2


def test_componenttools_split_component_by_duration_23():
    r'''Split measure with power-of-two time signature denominator 
    with multiplied leaves. Split at through-leaf offset with 
    power-of-two denominator. Leaf written durations stay the same 
    but multipliers change.
    '''

    staff = Staff()
    staff.append(Measure((2, 16), "c'8 d'8"))
    staff.append(Measure((2, 16), "e'8 f'8"))
    for leaf in staff.select_leaves():
        leaf.lilypond_duration_multiplier = Fraction(1, 2)
    spannertools.BeamSpanner(staff[0])
    spannertools.BeamSpanner(staff[1])
    spannertools.SlurSpanner(staff.select_leaves())

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 2/16
                c'8 * 1/2 [ (
                d'8 * 1/2 ]
            }
            {
                e'8 * 1/2 [
                f'8 * 1/2 ] )
            }
        }
        '''
        )

    halves = componenttools.split_component_by_duration(
        staff[0], 
        Duration(3, 32), 
        fracture_spanners=True, 
        tie_split_notes=False,
        )

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 3/32
                c'8 * 1/2 [ (
                d'8 * 1/4 ] )
            }
            {
                \time 1/32
                d'8 * 1/4 [ ] (
            }
            {
                \time 2/16
                e'8 * 1/2 [
                f'8 * 1/2 ] )
            }
        }
        '''
        )
        
    assert select(staff).is_well_formed()
    assert len(halves) == 2


def test_componenttools_split_component_by_duration_24():
    r'''Split measure with power-of-two time signature denominator 
    with multiplied leaves. Split at through-leaf offset without 
    power-of-two denominator. Leaf written durations adjust for change 
    from power-of-two denominator to non-power-of-two denominator.
    Leaf multipliers also change.
    '''

    staff = Staff()
    staff.append(Measure((2, 16), "c'8 d'8"))
    staff.append(Measure((2, 16), "e'8 f'8"))
    for leaf in staff.select_leaves():
        leaf.lilypond_duration_multiplier = Fraction(1, 2)
    spannertools.BeamSpanner(staff[0])
    spannertools.BeamSpanner(staff[1])
    spannertools.SlurSpanner(staff.select_leaves())

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 2/16
                c'8 * 1/2 [ (
                d'8 * 1/2 ]
            }
            {
                e'8 * 1/2 [
                f'8 * 1/2 ] )
            }
        }
        '''
        )

    halves = componenttools.split_component_by_duration(
        staff[0], 
        Duration(2, 24), 
        fracture_spanners=True, 
        tie_split_notes=False,
        )

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 2/24
                \scaleDurations #'(2 . 3) {
                    c'8. * 1/2 [ (
                    d'8. * 1/6 ] )
                }
            }
            {
                \time 1/24
                \scaleDurations #'(2 . 3) {
                    d'8. * 1/3 [ ] (
                }
            }
            {
                \time 2/16
                e'8 * 1/2 [
                f'8 * 1/2 ] )
            }
        }
        '''
        )

    assert select(staff).is_well_formed()
    assert len(halves) == 2


def test_componenttools_split_component_by_duration_25():
    r'''Split measure with power-of-two time signature denominator 
    with multiplied leaves. Time signature carries numerator that 
    necessitates ties. Split at through-leaf offset without 
    power-of-two denominator.
    '''

    staff = Staff([Measure((5, 16), "s1 * 5/16")])

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 5/16
                s1 * 5/16
            }
        }
        '''
        )

    halves = componenttools.split_component_by_duration(
        staff[0], 
        Duration(16, 80), 
        fracture_spanners=True,
        )

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 16/80
                \scaleDurations #'(4 . 5) {
                    s1 * 1/4
                }
            }
            {
                \time 9/80
                \scaleDurations #'(4 . 5) {
                    s1 * 9/64
                }
            }
        }
        '''
        )

    assert select(staff).is_well_formed()
    assert len(halves) == 2


def test_componenttools_split_component_by_duration_26():
    r'''Split measure without power-of-two time signature denominator
    at split offset without power-of-two denominator.
    Measure multiplier and split offset multiplier match.
    Split between leaves but do fracture spanners.
    '''

    measure = Measure((15, 80), "c'32 d' e' f' g' a' b' c''64")
    staff = Staff([measure])
    spannertools.BeamSpanner(staff[0])
    spannertools.SlurSpanner(staff.select_leaves())

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 15/80
                \scaleDurations #'(4 . 5) {
                    c'32 [ (
                    d'32
                    e'32
                    f'32
                    g'32
                    a'32
                    b'32
                    c''64 ] )
                }
            }
        }
        '''
        )

    halves = componenttools.split_component_by_duration(
        staff[0], 
        Duration(14, 80), 
        fracture_spanners=True,
        )

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 14/80
                \scaleDurations #'(4 . 5) {
                    c'32 [ (
                    d'32
                    e'32
                    f'32
                    g'32
                    a'32
                    b'32 ] )
                }
            }
            {
                \time 1/80
                \scaleDurations #'(4 . 5) {
                    c''64 [ ] ( )
                }
            }
        }
        '''
        )

    assert select(staff).is_well_formed()
    assert len(halves) == 2


def test_componenttools_split_component_by_duration_27():
    r'''Make sure tie (re)application happens only where sensible.
    '''

    halves = componenttools.split_component_by_duration(
        Container("c'4"), 
        Duration(3, 16), 
        fracture_spanners=True,
        )

    assert testtools.compare(
        halves[0][0],
        r'''
        {
            c'8.
        }
        '''
        )

    assert testtools.compare(
        halves[-1][0],
        r'''
        {
            c'16
        }
        '''
        )

    assert select(halves[0][0]).is_well_formed()
    assert select(halves[-1][0]).is_well_formed()
