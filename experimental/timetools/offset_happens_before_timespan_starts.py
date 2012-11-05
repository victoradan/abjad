def offset_happens_before_timespan_starts(timespan=None, offset=None, hold=False):
    r'''.. versionadded:: 1.0

    ::

        >>> from experimental import *

    Make offset inequality indicating that `offset` happens before `timespan` starts::

        >>> timetools.offset_happens_before_timespan_starts()
        OffsetInequality('offset < timespan.start')

    Make offset inequality indicating that offset ``1/2`` happens before `timespan` starts::

        >>> offset = durationtools.Offset(1, 2)

    ::

        >>> offset_inequality = timetools.offset_happens_before_timespan_starts(
        ...     offset=offset)

    ::

        >>> z(offset_inequality)
        timetools.OffsetInequality(
            'offset < timespan.start',
            offset=durationtools.Offset(1, 2)
            )

    Make offset inequality indicating that `offset` happens before timespan ``[2, 8)`` starts::

        >>> timespan = timetools.expr_to_timespan((2, 8))

    ::

        >>> offset_inequality = timetools.offset_happens_before_timespan_starts(
        ...     timespan=timespan)

    ::

        >>> z(offset_inequality)
        timetools.OffsetInequality(
            'offset < timespan.start',
            timespan=timetools.LiteralTimespan(
                start_offset=durationtools.Offset(2, 1),
                stop_offset=durationtools.Offset(8, 1)
                )
            )

    Make offset inequality indicating that offset ``1/2`` happens before 
    timespan ``[2, 8)`` starts::

        >>> offset_inequality = timetools.offset_happens_before_timespan_starts(
        ...     timespan=timespan, offset=offset, hold=True)

    ::

        >>> z(offset_inequality)
        timetools.OffsetInequality(
            'offset < timespan.start',
            timespan=timetools.LiteralTimespan(
                start_offset=durationtools.Offset(2, 1),
                stop_offset=durationtools.Offset(8, 1)
                ),
            offset=durationtools.Offset(1, 2)
            )

    Evaluate offset inequality indicating that offset ``1/2`` happens before 
    timespan ``[2, 8)`` starts::

        >>> timetools.offset_happens_before_timespan_starts(
        ...     timespan=timespan, offset=offset, hold=False)
        True

    Return offset inequality or boolean.
    '''
    from experimental import timetools

    offset_inequality = timetools.OffsetInequality(
        'offset < timespan.start',
        timespan=timespan, offset=offset)

    if offset_inequality.is_fully_loaded and not hold:
        return offset_inequality()
    else:
        return offset_inequality
