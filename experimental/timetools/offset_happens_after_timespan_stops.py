def offset_happens_after_timespan_stops(timespan=None, offset=None, hold=False):
    r'''.. versionadded:: 1.0

    ::

        >>> from experimental import *

    Make offset inequality indicating that `offset` happens after `timespan` stops::

        >>> timetools.offset_happens_after_timespan_stops()
        OffsetInequality('timespan.stop < offset')

    '''
    from experimental import timetools

    offset_inequality = timetools.OffsetInequality(
        'timespan.stop < offset',
        timespan=timespan, offset=offset)

    if offset_inequality.is_fully_loaded and not hold:
        return offset_inequality()
    else:
        return offset_inequality
