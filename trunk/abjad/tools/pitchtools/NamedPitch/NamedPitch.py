from abjad.cfg._read_config_file import _read_config_file
from abjad.core import _StrictComparator
from abjad.tools.pitchtools._Pitch import _Pitch


_accidental_spelling = _read_config_file( )['accidental_spelling']

class NamedPitch(_StrictComparator, _Pitch):
   '''Musical pitch.'''

   accidental_spelling = _accidental_spelling

   __slots__ = ('_accidental', '_deviation', '_letter', '_octave')

   def __new__(klass, *args):
      from abjad.tools import pitchtools
      self = object.__new__(klass)
      #self._deviation = None
      object.__setattr__(self, '_deviation', None)
      if not args:
         self._init_empty( )
      elif len(args) == 1 and isinstance(args[0], (int, long, float)):
         self._init_by_number(*args)
      elif len(args) == 1 and isinstance(args[0], NamedPitch):
         self._init_by_reference(*args)
      elif len(args) == 1 and pitchtools.is_named_pitch_pair(args[0]):
         self._init_by_pair(*args)
      elif len(args) == 1 and isinstance(args[0], str):
         self._init_by_pitch_string(*args)
      elif len(args) == 2 and isinstance(args[0], str):
         self._init_by_name_and_octave(*args)
      elif len(args) == 2 and isinstance(args[0], pitchtools.NamedPitchClass):
         self._init_by_named_pitch_class_and_octave_number(*args)
      elif len(args) == 2 and isinstance(args[0], (int, long, float)):
         if isinstance(args[1], str):
            self._init_by_number_and_letter(*args)
         elif isinstance(args[1], pitchtools.NamedPitchClass):
            self._init_by_number_and_named_pitch_class(*args)
         else:
            raise TypeError
      elif len(args) == 3:
         self._init_by_name_octave_and_deviation(*args)
      else:
         raise ValueError('%s not valid pitch token.' % str(args))
      return self

   def __getnewargs__(self):
      return (self.name, self.octave)

#   def __init__(self, *args):
#      from abjad.tools import pitchtools
#      #self._deviation = None
#      object.__setattr__(self, '_deviation', None)
#      if not args:
#         self._init_empty( )
#      elif len(args) == 1 and isinstance(args[0], (int, long, float)):
#         self._init_by_number(*args)
#      elif len(args) == 1 and isinstance(args[0], NamedPitch):
#         self._init_by_reference(*args)
#      elif len(args) == 1 and pitchtools.is_named_pitch_pair(args[0]):
#         self._init_by_pair(*args)
#      elif len(args) == 1 and isinstance(args[0], str):
#         self._init_by_pitch_string(*args)
#      elif len(args) == 2 and isinstance(args[0], str):
#         self._init_by_name_and_octave(*args)
#      elif len(args) == 2 and isinstance(args[0], pitchtools.NamedPitchClass):
#         self._init_by_named_pitch_class_and_octave_number(*args)
#      elif len(args) == 2 and isinstance(args[0], (int, long, float)):
#         if isinstance(args[1], str):
#            self._init_by_number_and_letter(*args)
#         elif isinstance(args[1], pitchtools.NamedPitchClass):
#            self._init_by_number_and_named_pitch_class(*args)
#         else:
#            raise TypeError
#      elif len(args) == 3:
#         self._init_by_name_octave_and_deviation(*args)
#      else:
#         raise ValueError('%s not valid pitch token.' % str(args))

   ## OVERLOADS ##

   def __add__(self, melodic_interval):
      '''.. versionadded:: 1.1.2'''
      from abjad.tools import pitchtools
      return pitchtools.transpose_pitch_by_melodic_interval(self, melodic_interval)

   def __copy__(self):
      '''.. versionadded:: 1.1.2'''
      return NamedPitch(self)

   def __eq__(self, arg):
      if isinstance(arg, NamedPitch):
         if self.altitude == arg.altitude:
            if self.accidental.semitones == arg.accidental.semitones:
               if self.deviation == arg.deviation:
                  return True
      return False

   def __ge__(self, arg):
      if not isinstance(arg, NamedPitch):
         #raise ValueError
         return False
      return self.altitude > arg.altitude or \
         (self.altitude == arg.altitude and \
         self.accidental.semitones >= arg.accidental.semitones) or \
         (self.altitude == arg.altitude and \
         self.accidental == arg.accidental and \
         self._deviation_numeric >= arg._deviation_numeric)

   def __gt__(self, arg):
      if not isinstance(arg, NamedPitch):
         raise ValueError
      return self.altitude > arg.altitude or \
         (self.altitude == arg.altitude and \
         self.accidental.semitones > arg.accidental.semitones) or \
         (self.altitude == arg.altitude and \
         self.accidental == arg.accidental and \
         self._deviation_numeric > arg._deviation_numeric)

   def __hash__(self):
      return hash(repr(self))

   def __le__(self, arg):
      if not isinstance(arg, NamedPitch):
         #raise ValueError
         return False
      if not self.altitude == arg.altitude:
         return self.altitude <= arg.altitude
      if not self.accidental == arg.accidental:
         return self.accidental <= arg.accidental
      return self._deviation_numeric <= arg._deviation_numeric

   def __lt__(self, arg):
      if not isinstance(arg, NamedPitch):
         #raise ValueError
         return False
      return self.altitude < arg.altitude or \
         (self.altitude == arg.altitude and \
         self.accidental.semitones < arg.accidental.semitones) or \
         (self.altitude == arg.altitude and \
         self.accidental == arg.accidental and \
         self._deviation_numeric < arg._deviation_numeric)

   def __ne__(self, arg):
      return not self == arg

   def __repr__(self):
      if self.name and not self.octave is None:
         if self.deviation is None:
            return '%s(%s, %s)' % (self.__class__.__name__, self.name, self.octave)
         else:
            return '%s(%s, %s, %s)' % (self.__class__.__name__,
               self.name, self.octave, self.deviation)
      else:
         return '%s( )' % self.__class__.__name__

   def __str__(self):
      if self.name and not self.octave is None:
         return '%s%s' % (self.name, self.ticks)
      else:
         return ''

   def __sub__(self, arg):
      from abjad.tools import pitchtools
      if isinstance(arg, NamedPitch):
         return pitchtools.calculate_melodic_diatonic_interval_from_named_pitch_to_named_pitch(
            self, arg)
      else:
         interval = arg
         return pitchtools.transpose_pitch_by_melodic_interval(self, -interval)

   ## PRIVATE ATTRIBUTES ##

   @property
   def _deviation_numeric(self):
      if self.deviation is None:
         return 0
      else:
         return self.deviation

   ## PRIVATE METHODS ##

   def _init_by_name_and_octave(self, name, octave):
      from abjad.tools import pitchtools
      letter = name[0]
      accidental_string = name[1:]
      #self.letter = letter
      #self.accidental = pitchtools.Accidental(accidental_string)
      #self.octave = octave
      object.__setattr__(self, '_letter', letter)
      object.__setattr__(self, '_accidental', pitchtools.Accidental(accidental_string))
      object.__setattr__(self, '_octave', octave)

   def _init_by_name_octave_and_deviation(self, name, octave, deviation):
      self._init_by_name_and_octave(name, octave)
      #self.deviation = deviation
      object.__setattr__(self, '_deviation', deviation)

   def _init_by_named_pitch_class_and_octave_number(self, npc, octave_number):
      self._init_by_name_and_octave(npc.name, octave_number)

   def _init_by_number(self, number):
      from abjad.tools import pitchtools
      spelling = self.accidental_spelling
      triple = pitchtools.pitch_number_to_pitch_letter_alphabetic_accidental_string_and_octave_number_triple(number, spelling)
      letter, accidental_string, octave = triple
      #self.letter = letter
      #self.accidental = pitchtools.Accidental(accidental_string)
      #self.octave = octave
      object.__setattr__(self, '_letter', letter)
      object.__setattr__(self, '_accidental', pitchtools.Accidental(accidental_string))
      object.__setattr__(self, '_octave', octave)

   def _init_by_number_and_letter(self, number, letter):
      from abjad.tools import pitchtools
      pair = pitchtools.number_letter_to_accidental_octave(number, letter)
      accidental_string, octave = pair
      #self.letter = letter
      #self.accidental = pitchtools.Accidental(accidental_string)
      #self.octave = octave
      object.__setattr__(self, '_letter', letter)
      object.__setattr__(self, '_accidental', pitchtools.Accidental(accidental_string))
      object.__setattr__(self, '_octave', octave)

   def _init_by_number_and_named_pitch_class(self, pitch_number, npc):
      letter = npc.name[:1]
      self._init_by_number_and_letter(pitch_number, letter)

   def _init_by_pair(self, pair):
      from abjad.tools import pitchtools
      name, octave = pair
      letter = name[0]
      accidental_string = name[1:]
      #self.letter = letter
      #self.accidental = pitchtools.Accidental(accidental_string)
      #self.octave = octave
      object.__setattr__(self, '_letter', letter)
      object.__setattr__(self, '_accidental', pitchtools.Accidental(accidental_string))
      object.__setattr__(self, '_octave', octave)

   def _init_by_pitch_string(self, pitch_string):
      from abjad.tools import pitchtools
      name = pitchtools.pitch_name_to_pitch_class_name(pitch_string)
      octave_number = pitchtools.pitch_name_to_octave_number(pitch_string)
      self._init_by_name_and_octave(name, octave_number)

   def _init_by_reference(self, pitch):
      from abjad.tools import pitchtools
      #self.letter = pitch.letter
      #self.accidental = pitchtools.Accidental(pitch.accidental.alphabetic_string)
      #self.octave = pitch.octave
      object.__setattr__(self, '_letter', pitch.letter)
      accidental = pitchtools.Accidental(pitch.accidental.alphabetic_string)
      object.__setattr__(self, '_accidental', accidental)
      object.__setattr__(self, '_octave', pitch.octave)

   def _init_empty(self):
      #self.letter = None
      #self.accidental = None
      #self.octave = None
      object.__setattr__(self, '_letter', None)
      object.__setattr__(self, '_accidental', None)
      object.__setattr__(self, '_octave', None)

   ## PUBLIC ATTRIBUTES ##

   @property
   def absolute_diatonic_scale_degree(self):
      return 7 * self.octave + self.degree

#   @apply
#   def accidental( ):
#      def fget(self):
#         '''Read / write reference to any accidental attaching to pitch.'''
#         return self._accidental
#      def fset(self, expr):
#         from abjad.tools import pitchtools
#         if expr is None:
#            self._accidental = pitchtools.Accidental('')
#         elif isinstance(expr, str):
#            self._accidental = pitchtools.Accidental(expr)
#         elif isinstance(expr, pitchtools.Accidental):
#            self._accidental = expr
#         else:
#            raise ValueError('can not set accidental.')
#      return property(**locals( ))

   @property
   def accidental(self):
      return self._accidental

   @property
   def altitude(self):
      '''See :term:`altitude`.'''
      if self.letter:
         return (self.octave - 4) * 7 + self.degree - 1
      else:
         return None
      
   @property
   def degree(self):
      '''Diatonic scale degree with ``1`` for C, ``2`` for D, etc.'''
      from abjad.tools.pitchtools.pitch_letter_to_one_indexed_diatonic_scale_degree_number \
         import pitch_letter_to_one_indexed_diatonic_scale_degree_number
      if self.letter:
         return pitch_letter_to_one_indexed_diatonic_scale_degree_number(self.letter)
      else:
         return None

#   @apply
#   def deviation( ):
#      def fget(self):
#         '''Read / write number of cents by which pitch deviates
#            from 12-ET intonation.'''
#         return self._deviation
#      def fset(self, arg):
#         assert isinstance(arg, (int, float, type(None)))
#         self._deviation = arg
#      return property(**locals( ))

   @property
   def deviation(self):
      return self._deviation

   @property
   def format(self):
      '''Read-only LilyPond format of pitch.'''
      return str(self)

   @property
   def letter(self):
      return self._letter

#   @apply
#   def name( ):
#      def fget(self):
#         '''Read / write letter and accidental of pitch concatenated
#         as a single string.'''
#         if self.letter and self.accidental:
#            return '%s%s' % (self.letter, self.accidental)
#         else:
#            return None
#      def fset(self, name):
#         from abjad.tools.pitchtools.pitch_name_to_pitch_letter_and_alphabetic_accidetnal_string_pair \
#            import pitch_name_to_pitch_letter_and_alphabetic_accidetnal_string_pair
#         letter, accidental = pitch_name_to_pitch_letter_and_alphabetic_accidetnal_string_pair(name)
#         self.letter = letter
#         self.accidental = accidental
#      return property(**locals( ))

   @property
   def name(self):
      if self.letter and self.accidental:
         return '%s%s' % (self.letter, self.accidental)
      else:
         return None

   @property
   def named_pitch_class(self):
      from abjad.tools import pitchtools
      return pitchtools.NamedPitchClass(self.name)

#   @apply
#   def number( ):
#      def fget(self):
#         '''Read / write numeric value of pitch
#         with middle C equal to ``0``.'''
#         from abjad.tools.pitchtools.pitch_letter_to_pitch_class_number import pitch_letter_to_pitch_class_number
#         if not self.octave is None:
#            if self.letter:
#               if self.accidental:
#                  octave = 12 * (self.octave - 4)
#                  pc = pitch_letter_to_pitch_class_number(self.letter)
#                  semitones = self.accidental.semitones
#                  return octave + pc + semitones
#         else:
#            return None
#      def fset(self, arg):
#         self.__init__(arg)
#      return property(**locals( ))

   @property
   def number(self):
      '''Read / write numeric value of pitch with middle C equal to ``0``.'''
      from abjad.tools.pitchtools.pitch_letter_to_pitch_class_number import pitch_letter_to_pitch_class_number
      if not self.octave is None:
         if self.letter:
            if self.accidental:
               octave = 12 * (self.octave - 4)
               pc = pitch_letter_to_pitch_class_number(self.letter)
               semitones = self.accidental.semitones
               return octave + pc + semitones
      else:
         return None

   @property
   def octave(self):
      return self._octave

   @property
   def pair(self):
      '''Read-only ``(name, octave)`` pair of pitch.'''
      if self.name and self.octave is not None:
         return (self.name, self.octave)
      else:
         return None

   @property
   def pc(self):
      '''Read-only pitch-class corresponding to pitch.

      .. note:: 
         deprecated. Use `pitch_class` instead.
      '''
      from abjad.tools import pitchtools
      number = self.number
      if number is not None:
         return pitchtools.NumericPitchClass(number % 12)
      else:
         return None
      

   @property
   def pitch_class(self):
      '''Read-only pitch-class corresponding to pitch.

      .. versionchanged:: 1.1.2
         now returns Abjad pitch-class instance instead of number.'''
      from abjad.tools import pitchtools
      number = self.number
      if number is not None:
         return pitchtools.NumericPitchClass(number % 12)
      else:
         return None

   @property
   def semitones(self):
      '''Read-only number of semitones to which pitch is equal.'''
      return self.number

   @property
   def ticks(self):
      '''Read-only European indicator of octave of pitch with
      the octave of middle C equal to a single ``'`` tick.'''
      if self.octave is not None:
         if self.octave <= 2:
            return ',' * (3 - self.octave)
         elif self.octave == 3:
            return ''
         else:
            return "'" * (self.octave - 3)
      else:
         return None

   ## PUBLIC METHODS ##

   def apply_accidental(self, accidental = None):
      '''Apply accidental and emit new pitch instance.'''
      from abjad.tools.pitchtools.Accidental import Accidental
      accidental = Accidental(accidental)
      new_accidental = self.accidental + accidental
      new_name = self.letter + new_accidental.alphabetic_string
      return type(self)(new_name, self.octave)
