from abjad.core.spanner import _Spanner
from abjad.helpers.leaf_split import leaf_split_binary, leaf_split
from abjad.helpers.leaves_fuse import leaves_fuse_binary
from abjad.meter.meter import _Meter
from abjad.rational.rational import Rational
from abjad.skip.skip import Skip
from abjad.tie.spanner import Tie


class MetricGrid(_Spanner):
   '''MetricGrid is a list of MetricStrips.'''
   def __init__(self, music, meters):
      _Spanner.__init__(self, music)
      self._meters = meters
      self.hide = False
#      self.offset ?

   @apply
   def meters( ):
      def fget(self):
         i = 0
         moffset = 0
         prev_meter = None
         while moffset < self.duration:
            m = self._meters[i % len(self._meters)]
            m = _Meter(*m)
            ### new attribute
            m.offset = moffset
            if prev_meter and prev_meter.pair == m.pair:
               m.hide = True
            yield m
            moffset += m.duration
            i += 1
            prev_meter = m
      def fset(self, meters):
         assert isinstance(meters, list)
         self._meters = meters
      return property(**locals( ))
         
   def splittingCondition(self, leaf):
      '''User definable conditioning function.'''
      return True

   def splitOnBar(self):
      leaf = self[0]
      meters = self.meters
      meter = meters.next( )
      while leaf:
         if leaf.offset < meter.offset:
            if leaf.offset + leaf.duration.prolated > meter.offset and \
               self.splittingCondition(leaf):
               ### will split
               if not leaf.tie.spanner:
                  Tie(leaf)
               splitdur = meter.offset - leaf.offset
               ### if splitdur not m / 2**n
               if not splitdur._denominator & (splitdur._denominator - 1):
                  leaves_splitted = leaf_split_binary(splitdur, leaf)
                  leaf = leaves_splitted[1][0]
               else:
                  leaves_splitted = leaf_split(splitdur, leaf)
                  leaf = leaves_splitted[1].leaves[0]
            else:
               ### only advance if we have not split.
               ### TODO _nextBead does not seem to play well with tuplets
               leaf = leaf._navigator._nextBead
               #leaf = leaf.next
         else:
            try:
               meter = meters.next( )
            except StopIteration:
               break 
      self._fuseTiedLeavesWithinMeasures( )

   def _fuseTiedLeavesWithinMeasures(self):
      ### fuse tied notes
      meters = self.meters
      meter = meters.next( )
      leaves_in_meter = [[]]
      leaf = self[0]
      ### group leaves by measure.
      while leaf:
         if leaf.offset < meter.offset + meter.duration:
            leaves_in_meter[-1].append(leaf)
            leaf = leaf._navigator._nextBead
         else:
            try:
               meter = meters.next( )
               leaves_in_meter.append([])
            except StopIteration:
               break
      ### group together leaves in same measure that are tied together.
      for leaves in leaves_in_meter:
         result = [[]]
         sp = leaves[0].tie.spanner
         for l in leaves:
            if l.tie.spanner and l.tie.spanner == sp:
               result[-1].append(l)
            else:
               sp = l.tie.spanner
               result.append([])
         ### fuse leaves 
         for r in result:
            ### keep last after graces, if any
            ### TODO: this is very hacky. Find better solution
            if len(r) > 0:
               r[0].grace.after = r[-1].grace.after
            leaves_fuse_binary(r)
         
   def _slicingMeters(self, leaf):
      '''Return the MetricStrip(s) that slices leaf, if any.'''
      for m in self.meters:
         if leaf.offset < m.offset:
            if leaf.offset + leaf.duration.prolated > m.offset:
               yield m 
            else:
               break

   def _matchingMeter(self, leaf):
      '''Return the MetricStrip for which meter.offset == leaf.offset'''
      for m in self.meters:
         if leaf.offset == m.offset: 
            return m


   ### FORMATTING ### 

   ###FIXME: formatting is ridiculously slow. 
   ###       find a way to make it faster.
   def _before(self, leaf):
      result = [ ]
      if not self.hide:
         meter = self._matchingMeter(leaf)
         if meter and not meter.hide:
            result.append(meter.lily)
            #return result
         m = self._slicingMeters(leaf)
         m = [meter for meter in m if not meter.hide]
         if m:
            result.append('<<')
            for meter in m:
               s = Skip( 1 )
               s.duration.multiplier = meter.offset - leaf.offset
               s.formatter.right.append(meter.lily)
               #result.append( '<<\n\t%s' % Sequential([s]).format )
               result.append( '{ %s }' % s.format )
      return result

   def _after(self, leaf):
      result = [ ]
      if not self.hide:
         m = self._slicingMeters(leaf)
         if any([not meter.hide for meter in m]):
            result.append( '>>' )
      return result


