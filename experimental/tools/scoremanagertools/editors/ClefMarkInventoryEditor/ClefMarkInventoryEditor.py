# -*- encoding: utf-8 -*-
from abjad.tools import contexttools
from experimental.tools.scoremanagertools import iotools
from experimental.tools.scoremanagertools.editors.ClefMarkEditor \
    import ClefMarkEditor
from experimental.tools.scoremanagertools.editors.ObjectInventoryEditor \
    import ObjectInventoryEditor
from experimental.tools.scoremanagertools.editors.TargetManifest \
    import TargetManifest
from experimental.tools.scoremanagertools.editors.TempoMarkEditor \
    import TempoMarkEditor


class ClefMarkInventoryEditor(ObjectInventoryEditor):

    ### CLASS VARIABLES ###

    item_class = contexttools.ClefMark

    item_editor_class = ClefMarkEditor

    item_getter_configuration_method = iotools.UserInputGetter.append_clef

    item_identifier = 'clef mark'

    target_manifest = TargetManifest(
        contexttools.ClefMarkInventory,
        target_name_attribute='name',
        )
