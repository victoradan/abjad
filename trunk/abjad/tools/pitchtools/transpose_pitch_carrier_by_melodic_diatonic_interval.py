from abjad.components import Chord
from abjad.components import Note
from abjad.tools import componenttools
from abjad.tools.pitchtools.MelodicDiatonicInterval import MelodicDiatonicInterval
from abjad.tools.pitchtools.NamedChromaticPitch.NamedChromaticPitch import NamedChromaticPitch
from abjad.tools.pitchtools.one_indexed_diatonic_scale_degree_number_to_diatonic_pitch_class_name import one_indexed_diatonic_scale_degree_number_to_diatonic_pitch_class_name


def transpose_pitch_carrier_by_melodic_diatonic_interval(pitch_carrier, melodic_diatonic_interval):
   '''.. versionadded:: 1.1.2

   Transpose `pitch_carrier` by `melodic_diatonic_interval`::

      abjad> pitch = NamedChromaticPitch(12)
      abjad> mdi = pitchtools.MelodicDiatonicInterval('minor', -3)
      abjad> pitchtools.transpose_pitch_carrier_by_melodic_diatonic_interval(pitch, mdi)
      NamedChromaticPitch(a, 4)

   Return named chromatic pitch.
   '''

   if not isinstance(melodic_diatonic_interval, MelodicDiatonicInterval):
      raise TypeError('must be melodic diatonic interval.')

   if isinstance(pitch_carrier, NamedChromaticPitch):
      return _transpose_pitch_by_melodic_diatonic_interval(
         pitch_carrier, melodic_diatonic_interval)
   elif isinstance(pitch_carrier, Note):
      new_note = componenttools.clone_components_and_remove_all_spanners([pitch_carrier])[0]
      new_pitch = _transpose_pitch_by_melodic_diatonic_interval(
         pitch_carrier.pitch, melodic_diatonic_interval)
      new_note.pitch = new_pitch
      return new_note
   elif isinstance(pitch_carrier, Chord):
      new_chord = componenttools.clone_components_and_remove_all_spanners([pitch_carrier])[0]
      for new_nh, old_nh in zip(
         new_chord.note_heads, pitch_carrier.note_heads):
         new_pitch = _transpose_pitch_by_melodic_diatonic_interval(
            old_nh.pitch, melodic_diatonic_interval)
         new_nh.pitch = new_pitch
      return new_chord
   else:
      raise TypeError('must be pitch, note or chord: %s' % str(pitch_carrier))


def _transpose_pitch_by_melodic_diatonic_interval(
   pitch, melodic_diatonic_interval):
   if not isinstance(pitch, NamedChromaticPitch):
      raise TypeError('must be pitch.')
   chromatic_pitch_number = \
      abs(pitch.numbered_chromatic_pitch) + melodic_diatonic_interval.semitones
   diatonic_scale_degree = \
      (pitch.numbered_diatonic_pitch_class._diatonic_pitch_class_number + 1) + \
      melodic_diatonic_interval.staff_spaces
   letter = one_indexed_diatonic_scale_degree_number_to_diatonic_pitch_class_name(
      diatonic_scale_degree)
   return NamedChromaticPitch(chromatic_pitch_number, letter)
