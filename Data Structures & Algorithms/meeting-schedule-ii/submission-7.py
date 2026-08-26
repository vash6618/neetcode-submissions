"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def overlap(self, int1, int2):
        if int2.start >= int1.end or int1.start >= int2.end:
            return False
        return True 

    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        sorted_arr = []
        for val in intervals:
            sorted_arr.append((val.start, 's'))
            sorted_arr.append((val.end, 'e'))
        sorted_arr.sort()
        meeting_cnt, rooms = 0, 0
        for val in sorted_arr:
            if val[1] == 's':
                meeting_cnt += 1
                rooms = max(rooms, meeting_cnt)
            else:
                meeting_cnt -= 1
            
        return rooms

