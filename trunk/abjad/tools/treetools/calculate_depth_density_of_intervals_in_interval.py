from fractions import Fraction
from abjad.tools.treetools.BoundedInterval import BoundedInterval
from abjad.tools.treetools.IntervalTree import IntervalTree
from abjad.tools.treetools.all_are_intervals_or_trees_or_empty \
   import all_are_intervals_or_trees_or_empty
from abjad.tools.treetools.compute_depth_of_intervals_in_interval \
   import compute_depth_of_intervals_in_interval


def calculate_depth_density_of_intervals_in_interval(intervals, interval):
   '''Return a Fraction, of the magnitude of each interval in the
   depth tree of `intervals` within `interval`, multiplied by the depth at that interval,
   divided by the overall magnitude of `intervals`.
   '''

   assert all_are_intervals_or_trees_or_empty(intervals)
   assert isinstance(interval, BoundedInterval)
   if isinstance(intervals, IntervalTree):
      tree = intervals
   else:
      tree = IntervalTree(intervals)
   depth = compute_depth_of_intervals_in_interval(tree, interval)

   return Fraction(sum([x.magnitude * x.data['depth'] for x in depth])) \
      / depth.magnitude
