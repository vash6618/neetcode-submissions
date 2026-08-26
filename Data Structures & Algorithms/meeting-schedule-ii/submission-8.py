"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = [val.start for val in intervals]
        ends = [val.end for val in intervals]
        starts.sort()
        ends.sort()
        s1, e1 = 0, 0
        active, rooms = 0, 0
        while s1 < len(starts):
            if ends[e1] <= starts[s1]:
                active -= 1
                e1+=1
            else:
                active += 1
                s1+=1
                rooms = max(rooms, active)
        return rooms

