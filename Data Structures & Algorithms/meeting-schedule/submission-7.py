"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # handle edge case
        if not intervals:
            return True
    
        #sort by start point
        intervals.sort(key=lambda x: x.start)
        #if start point of current interval is <= endpoint of last interval, return false   
        meeting_num = 0
        previous_endpoint = intervals[meeting_num].end
        # if any meetings start before any end, there's a conflict
        for meeting in intervals[1::]:
            if meeting.start < previous_endpoint:
                return False
            meeting_num+=1
            previous_endpoint = intervals[meeting_num].end
        return True