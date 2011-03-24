from fractions import Fraction
from abjad.tools.treetools.IntervalTree import IntervalTree
from abjad.tools.treetools.all_are_intervals_or_trees_or_empty \
   import all_are_intervals_or_trees_or_empty



def calculate_mean_attack_of_intervals(intervals):
   '''Return Fraction of the average attack offset of `intervals`'''

   assert all_are_intervals_or_trees_or_empty(intervals)
   if isinstance(intervals, IntervalTree):
      tree = intervals
   else:
      tree = IntervalTree(intervals)
   if not tree:
      return None
   return Fraction(sum([i.low for i in tree])) / len(tree)

