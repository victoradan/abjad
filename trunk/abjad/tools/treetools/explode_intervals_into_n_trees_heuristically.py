from fractions import Fraction
from abjad.tools.treetools.BoundedInterval import BoundedInterval
from abjad.tools.treetools.IntervalTree import IntervalTree
from abjad.tools.treetools.all_are_intervals_or_trees_or_empty \
   import all_are_intervals_or_trees_or_empty
from abjad.tools.treetools.calculate_depth_density_of_intervals_in_interval \
   import calculate_depth_density_of_intervals_in_interval
from abjad.tools.treetools.compute_logical_or_of_intervals \
   import compute_logical_or_of_intervals


def explode_intervals_into_n_trees_heuristically(intervals, n):
   '''Explode `intervals` into `n` trees, avoiding overlap when possible,
   and distributing intervals so as to equalize density across the trees.
   '''

   assert all_are_intervals_or_trees_or_empty(intervals)
   assert isinstance(n, int) and 0 < n
   if isinstance(intervals, IntervalTree):
      tree = intervals
   else:
      tree = IntervalTree(intervals)

   if not tree:
      return [IntervalTree([ ])] * n
   elif n == 1:
      return [tree]

   # cache
   treebounds = BoundedInterval(tree.low, tree.high)
   xtrees = [IntervalTree(tree[0])]
   densities = [calculate_depth_density_of_intervals_in_interval(xtrees[0], treebounds)]
   logical_ors = [compute_logical_or_of_intervals(xtrees[0])]
   for i in range(1, n):
      xtrees.append(IntervalTree([ ]))
      densities.append(0)
      logical_ors.append(IntervalTree([ ]))

   # loop through intervals
   for interval in tree[1:]:

      empty_trees = [ ]
      nonoverlapping_trees = [ ]
      overlapping_trees = [ ]

      for i, zipped in enumerate(zip(xtrees, densities, logical_ors)):
         xtree = zipped[0]
         density = zipped[1]
         logical_or = zipped[2]
         if not len(xtree):
            empty_trees.append((i, xtree, density, logical_or))
            break
         elif not logical_or[-1].is_overlapped_by_interval(interval):
            nonoverlapping_trees.append((i, xtree, density, logical_or))
         else:
            overlapping_trees.append((i, xtree, density, logical_or))

      if len(empty_trees):
         i = empty_trees[0][0]
      elif len(nonoverlapping_trees):
         nonoverlapping_trees = sorted(nonoverlapping_trees, key = lambda x: x[2])
         i = nonoverlapping_trees[0][0]
      else:
         overlapping_trees = sorted(overlapping_trees, \
            key = lambda x: x[3][-1].get_overlap_with_interval(interval))
         overlapping_trees = filter( \
            lambda x: x[3][-1].magnitude == overlapping_trees[0][3][-1].magnitude,
            overlapping_trees)
         i = overlapping_trees[0][0]

      xtrees[i]._insert(interval)
      densities[i] = calculate_depth_density_of_intervals_in_interval(xtrees[i], treebounds)
      logical_ors[i] = compute_logical_or_of_intervals(xtrees[i])

   return xtrees
