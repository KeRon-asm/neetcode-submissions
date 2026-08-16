class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0 # start a counter of intervals that overlap
        prevEnd = intervals[0][1] # set prev_end =  the endpoint of the first sorted interval

        for start, end in intervals[1:]: # iterate through the intervals keeping track of start and endpoint
            if start >= prevEnd: # if the current start is greater than or equal to the previous end
            # i.e, they overlap
                prevEnd = end # merge   
            else:
                res += 1 # if they don't overlap, increase counter
                prevEnd = min(end, prevEnd) # make the previous interval as small as possible, so as to catch s many potential overlaps as possible
        return res