from abjad.tools import contexttools
from abjad.tools import instrumenttools
from abjad.tools import scoretools
from abjad.tools import stafftools
from abjad.tools import voicetools
from abjad.tools.scoretemplatetools.ScoreTemplate import ScoreTemplate
import collections


class GroupedRhythmicStavesScoreTemplate(ScoreTemplate):
    r'''.. versionadded:: 2.9

    Grouped rhythmic staves score template::

        abjad> from abjad.tools import scoretemplatetools

    ::

        abjad> template = scoretemplatetools.GroupedRhythmicStavesScoreTemplate(4)
        abjad> score = template()

    ::

        abjad> score
        Score-"Grouped Rhythmic Staves Score"<<1>>

    ::

        abjad> f(score)
        \context Score = "Grouped Rhythmic Staves Score" <<
            \context StaffGroup = "Grouped Rhythmic Staves Staff Group" <<
                \context RhythmicStaff = "Staff 1" {
                    \context Voice = "Voice 1" {
                    }
                }
                \context RhythmicStaff = "Staff 2" {
                    \context Voice = "Voice 2" {
                    }
                }
                \context RhythmicStaff = "Staff 3" {
                    \context Voice = "Voice 3" {
                    }
                }
                \context RhythmicStaff = "Staff 4" {
                    \context Voice = "Voice 4" {
                    }
                }
            >>
        >>

    Return score template object.   
    '''

    ### INITIALIZER ###

    def __init__(self, n=2):
        self.context_name_abbreviations = collections.OrderedDict()
        self.n = n

    ### SPECIAL METHODS ###

    def __call__(self):
        staves = []
        for index in range(self.n):
            number = index + 1
            voice = voicetools.Voice(name='Voice {}'.format(number))     
            staff = stafftools.RhythmicStaff([voice], name='Staff {}'.format(number))
            staves.append(staff)
            self.context_name_abbreviations['v{}'.format(number)] = voice
        
        grouped_rhythmic_staves_staff_group = scoretools.StaffGroup(
            staves, name='Grouped Rhythmic Staves Staff Group')         

        grouped_rhythmic_staves_score = scoretools.Score(
            [grouped_rhythmic_staves_staff_group], name='Grouped Rhythmic Staves Score')

        return grouped_rhythmic_staves_score
