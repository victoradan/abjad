from abjad.tools.treetools.IntervalTree import IntervalTree
from abjad.tools.treetools.all_are_intervals_or_trees_or_empty import all_are_intervals_or_trees_or_empty
from fractions import Fraction


def scale_interval_magnitudes_to_rational(intervals, rational):
   '''Scale the magnitude of each interval in `intervals` to
   `rational`, maintaining their low offsets ::

      abjad> from abjad.tools import treetools
      abjad> from abjad.tools.treetools import BoundedInterval
      abjad> from abjad.tools.treetools import IntervalTree

   ::

      abjad> a = BoundedInterval(-1, 3)
      abjad> b = BoundedInterval(6, 12)
      abjad> c = BoundedInterval(9, 16)
      abjad> tree = IntervalTree([a, b, c])
      abjad> treetools.scale_interval_magnitudes_to_rational(tree, Fraction(1, 7))
      IntervalTree([
         BoundedInterval(-1, Fraction(-6, 7), {}),
         BoundedInterval(6, Fraction(43, 7), {}),
         BoundedInterval(9, Fraction(64, 7), {})
      ])

   Return interval tree.
   '''

   assert isinstance(rational, (int, Fraction)) and 0 < rational
   assert all_are_intervals_or_trees_or_empty(intervals)
   if isinstance(intervals, IntervalTree):
      tree = intervals
   else:
      tree = IntervalTree(intervals)
   if not tree:
      return tree

   return IntervalTree([
      x.scale_to_rational(rational) for x in tree
   ])
