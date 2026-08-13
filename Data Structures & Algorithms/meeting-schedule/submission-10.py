"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #sort
        intervals.sort(key=lambda x: x.start)

        for i in range(1,len(intervals)): #start from the second element
            faster = intervals
            if faster[i-1].end > faster[i].start:
                return False
        return True