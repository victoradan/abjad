# -*- encoding: utf-8 -*-
from abjad.tools.abctools.ContextManager import ContextManager


class ControllerContext(ContextManager):
    r'''Controller context manager.
    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_session',
        '_controller',
        '_is_in_confirmation_environment',
        '_on_enter_callbacks',
        '_on_exit_callbacks',
        '_reset_hide_hidden_commands',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        controller=None,
        is_in_confirmation_environment=False,
        on_enter_callbacks=None,
        on_exit_callbacks=None,
        reset_hide_hidden_commands=True,
        ):
        self._controller = controller
        self._is_in_confirmation_environment = is_in_confirmation_environment
        self._on_enter_callbacks = on_enter_callbacks or ()
        self._on_exit_callbacks = on_exit_callbacks or ()
        self._reset_hide_hidden_commands = reset_hide_hidden_commands
        self._session = self._controller._session

    ### SPECIAL METHODS ###

    def __enter__(self):
        r'''Enters controller stack context manager.

        Returns none.
        '''
        self._session._controller_stack.append(self._controller)
        if self._controller not in self._session.controllers_visited:
            self._session._controllers_visited.append(self._controller)
        self._session._is_in_confirmation_environment = \
            self._is_in_confirmation_environment
        if self._reset_hide_hidden_commands:
            self._session._hide_hidden_commands = True
        for on_enter_callback in self._on_enter_callbacks:
            on_enter_callback()

    def __exit__(self, exg_type, exc_value, trackeback):
        r'''Exits controller stack context manager.

        Returns none.
        '''
        self._session._controller_stack.pop()
        self._session._is_in_confirmation_environment = False
        if self._reset_hide_hidden_commands:
            self._session._hide_hidden_commands = True
        for on_exit_callback in self._on_exit_callbacks:
            on_exit_callback()

    def __repr__(self):
        r'''Gets interpreter representation of context manager.

        Returns string.
        '''
        return '<{}({!r})>'.format(type(self).__name__, self._controller)