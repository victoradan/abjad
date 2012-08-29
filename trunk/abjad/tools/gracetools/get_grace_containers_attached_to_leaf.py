def get_grace_containers_attached_to_leaf(leaf, kind=None):
    r'''.. versionadded:: 2.0

    Example 1. Get all grace containers attached to `leaf`::

        >>> staff = Staff("c'8 d'8 e'8 f'8")
        >>> gracetools.GraceContainer([Note("cs'16")], kind='grace')(staff[1])
        Note("d'8")
        >>> gracetools.GraceContainer([Note("ds'16")], kind='after')(staff[1])
        Note("d'8")

    ::

        >>> f(staff)
        \new Staff {
            c'8
            \grace {
                cs'16
            }
            \afterGrace
            d'8
            {
                ds'16
            }
            e'8
            f'8
        }

    ::

        >>> gracetools.get_grace_containers_attached_to_leaf(staff[1])
        (GraceContainer(cs'16), GraceContainer(ds'16))

    Example 2. Get only (proper) grace containers attached to `leaf`::

        >>> gracetools.get_grace_containers_attached_to_leaf(staff[1], kind='grace')
        (GraceContainer(cs'16),)

    Example 3. Get only after grace containers attached to `leaf`::

        >>> gracetools.get_grace_containers_attached_to_leaf(staff[1], kind='after')
        (GraceContainer(ds'16),)

    Return tuple.
    '''

    result = []
    if kind in (None, 'grace') and hasattr(leaf, '_grace'):
        result.append(leaf._grace)
    if kind in (None, 'after') and hasattr(leaf, '_after_grace'):
        result.append(leaf._after_grace)
    return tuple(result)
