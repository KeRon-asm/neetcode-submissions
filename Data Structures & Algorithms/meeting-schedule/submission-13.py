"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        i = 0
        for item in intervals[1::]:
            prev_element = intervals[i]
            if item.start < prev_element.end:
                return False
            i+=1
        return True
