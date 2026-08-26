"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:(x.start,x.end))
        heap = []
        for val in intervals:
            if heap and heap[0] <= val.start:
                heapq.heappop(heap)
            heapq.heappush(heap, val.end)
        return len(heap)

