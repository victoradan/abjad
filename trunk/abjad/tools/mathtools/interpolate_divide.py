from abjad.core import Rational
from abjad.tools.mathtools.interpolate_cosine import interpolate_cosine
from abjad.tools.mathtools.interpolate_exponential import interpolate_exponential


def interpolate_divide(total, start_frac, stop_frac, exp='cosine'):
   '''Divide `total` into segments of sizes computed from interpolating 
   between `start_frac` and `stop_frac`::

      abjad> mathtools.interpolate_divide(10, 1, 1, exp=1)
      [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
      abjad> sum(_)
      10.0

   ::

      abjad> mathtools.interpolate_divide(10, 5, 1)
      [4.7986734489043181, 2.8792040693425909, 1.3263207210948171, 
      0.99580176065827419]
      abjad> sum(_)
      10.0 

   Set ``exp='cosine'`` for cosine interpolation.

   Set `exp` to a numeric value for exponential interpolation with `exp`
   as the exponent.

   Scale resulting segments so that their sum equals exactly `total`.

   Return a list of floats.

   .. versionchanged:: 1.1.2
      renamed ``interpolate.divide( )`` to
      ``mathtools.interpolate_divide( )``.
   '''

   if total <=0 :
      raise ValueError("'total' must be > 0.")
   if start_frac <= 0 or stop_frac <= 0:
      raise ValueError("Both 'start_frac' and 'stop_frac' must be > 0.")
   if (stop_frac + start_frac) > total:
      raise ValueError("'start_frac' + 'stop_frac' must be < 'total'.")

   result = [ ]
   total = float(total)
   partial_sum = 0
   while partial_sum < total:
      if exp == 'cosine':
         ip = interpolate_cosine(start_frac, stop_frac, partial_sum / total)
      else:
         ip = interpolate_exponential(start_frac, stop_frac, partial_sum / total, exp)
      result.append(ip)
      partial_sum += ip

   ## scale result to fit total exaclty
   result = [x * total / sum(result) for x in result]
   #result = [Rational(int(round(x * 10000, 5)), 10000) for x in result]
   return result

