from abjad.tools.pitchtools.list_named_chromatic_pitches_in_expr import list_named_chromatic_pitches_in_expr


def list_chromatic_pitch_numbers_in_expr(expr):
   '''.. versionadded:: 1.1.2

   List chromatic pitch numbers in `expr`::

      abjad> tuplet = tuplettools.FixedDurationTuplet((2, 8), macros.scale(3))
      abjad> pitchtools.list_chromatic_pitch_numbers_in_expr(tuplet)
      (0, 2, 4)

   Return tuple of zero or more numbers.
   '''

   pitches = list_named_chromatic_pitches_in_expr(expr)

   pitch_numbers = [pitch.numbered_chromatic_pitch._chromatic_pitch_number for pitch in pitches]
   pitch_numbers = tuple(pitch_numbers)

   return pitch_numbers
