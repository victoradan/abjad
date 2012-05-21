from abjad import *
import py.test


def testHarmonicObjectCounterpointInterval_semitones_01():
    '''Counterpoint intervals evaluate to no exact number of semitones.'''

    hcpi = pitchtools.HarmonicCounterpointInterval(15)

    assert py.test.raises(NotImplementedError, 'hcpi.semitones')
