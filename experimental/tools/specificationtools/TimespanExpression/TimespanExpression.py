from abjad.tools import timespantools
from experimental.tools.specificationtools.AnchoredExpression import AnchoredExpression
from experimental.tools.specificationtools.TimeContiguousSetMethodMixin import TimeContiguousSetMethodMixin
from experimental.tools.specificationtools.SelectMethodMixin import SelectMethodMixin
from experimental.tools.specificationtools.TimespanCallbackMixin import TimespanCallbackMixin


class TimespanExpression(AnchoredExpression, TimespanCallbackMixin, SelectMethodMixin, TimeContiguousSetMethodMixin):
    r'''Timespan expression.

    Preliminary definitions:

    ::

        >>> score_template = scoretemplatetools.GroupedRhythmicStavesScoreTemplate(staff_count=4)
        >>> score_specification = specificationtools.ScoreSpecificationInterface(score_template=score_template)
        >>> red_segment = score_specification.append_segment(name='red')
        >>> set_expression = red_segment.set_time_signatures([(4, 8), (3, 8)])
        >>> blue_segment = score_specification.append_segment(name='blue')
        >>> set_expression = blue_segment.set_time_signatures([(9, 16), (3, 16)])

    Timespan expressions are immutable.
    '''

    ### INITIALIZER ###

    def __init__(self, anchor=None, callbacks=None):
        from experimental.tools import specificationtools
        AnchoredExpression.__init__(self, anchor=anchor)
        TimespanCallbackMixin.__init__(self, callbacks=callbacks)

    ### PRIVATE METHODS ###

    def evaluate(self):
        '''Evaluate timespan expression.

        Return none when nonevaluable.

        Return timespan when evaluable.
        '''
        from experimental.tools import specificationtools
        result = self._evaluate_anchor_timespan()
        if result is None:
            return
        elif isinstance(result, timespantools.Timespan):
            timespan = self._apply_callbacks(result)
            expression = specificationtools.IterablePayloadExpression([timespan])
            return expression
        elif isinstance(result, list):
            timespan_expressions = []
            for timespan in result:
                timespan = self._apply_callbacks(timespan)
                expression = specificationtools.IterablePayloadExpression([timespan])
                timespan_expressions.append(expression)
            assert len(result) == len(timespan_expressions)
            return timespan_expressions
        else:
            raise TypeError(result)
