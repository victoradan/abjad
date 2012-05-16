def get_improper_parentage_of_component_that_start_with_component(component):
    r'''.. versionadded:: 2.9

    Get improper parentage of `component` that start with `component`::

        abjad> staff = Staff(r"c' << \new Voice { d' } \new Voice { e' } >> f'")

    ::

        abjad> f(staff)
        \new Staff {
            c'4
            <<
                \new Voice {
                    d'4
                }
                \new Voice {
                    e'4
                }
            >>
            f'4
        }

    ::

        abjad> componenttools.get_improper_parentage_of_component_that_start_with_component(staff.leaves[1])
        [Note("d'4"), Voice{1}, <<Voice{1}, Voice{1}>>]

    Return list of `component` together with proper parentage that start with `component`.
    '''
    from abjad.tools import componenttools

    # initialize result
    result = []

    # add component
    result.append(component)

    # add proper parentage that start with component
    prev = component
    for parent in componenttools.get_proper_parentage_of_component(component):
        if parent.is_parallel:
            result.append(parent)
        elif parent.index(prev) == 0:
            result.append(parent)
        prev = parent

    # return result
    return result
