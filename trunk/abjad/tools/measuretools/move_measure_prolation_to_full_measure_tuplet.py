from abjad.tools import componenttools
from abjad.tools import containertools
from abjad.tools import durationtools
from abjad.tools import mathtools


def move_measure_prolation_to_full_measure_tuplet(expr):
    '''.. versionadded:: 2.0

    Move measure prolation to full-measure tuplet.

    Turn non-power-of-two measures into power-of-two measures containing 
    a single fixed-duration tuplet.

    Note that not all non-power-of-two measures can be made power-of-two.

    Returns None because processes potentially many measures.

    .. versionchanged:: 2.0
        renamed ``measuretools.project()`` to
        ``measuretools.move_measure_prolation_to_full_measure_tuplet()``.
    '''
    from abjad.tools import contexttools
    from abjad.tools import iterationtools
    from abjad.tools import timesignaturetools
    from abjad.tools import tuplettools

    for measure in iterationtools.iterate_measures_in_expr(expr):
        if contexttools.get_effective_time_signature(measure).has_non_power_of_two_denominator:

            # find meter and contents multipliers
            meter_multiplier = contexttools.get_effective_time_signature(measure).multiplier
            contents_multiplier = componenttools.get_likely_multiplier_of_components(measure[:])

            # update non-power-of-two meter to power-of-two
            power_of_two_time_signature = \
                timesignaturetools.time_signature_to_time_signature_with_power_of_two_denominator(
                contexttools.get_effective_time_signature(measure), contents_multiplier)
            contexttools.detach_time_signature_marks_attached_to_component(measure)
            power_of_two_time_signature.attach(measure)

            # find target duration and create tuplet
            target_duration = meter_multiplier * measure.contents_duration
            tuplet = tuplettools.FixedDurationTuplet(target_duration, measure[:])

            # scale tuplet contents, if helpful
            if contents_multiplier is not None:
                #containertools.scale_contents_of_container(tuplet, ~contents_multiplier)
                inverse_multiplier = durationtools.Duration(
                    contents_multiplier.denominator, contents_multiplier.numerator)
                containertools.scale_contents_of_container(tuplet, inverse_multiplier)
