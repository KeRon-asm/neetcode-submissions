class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #intervals are overlapping if they have a common endpoint
        #merge all common intervals
        #return an array of the non-overlapping intervals that cover all the intervals
        #First we need the intervals sorted by their start point in  ascending order
        intervals.sort(key=lambda x: x[0])  
        output = [intervals[0]] #output will at least be the first interval, if there's only one
        for item in intervals:
            lastEnd = output[-1][1] #this is the end point of the latest interval  
            
            #if end point of the soonest interval is greater than the start point of the latest interval, they overlap
            #if sooner's start is less than the later's end point, they overlap
            #The second logic works because the intervals are sorted by start point
            if item[0] <= lastEnd:
                #if they overlap, merge them
                output[-1][1] = max(item[1], lastEnd) #ensure the end point is the largest of the two intervals
            else: # if they don't overlap
                output.append(item)
        return output
