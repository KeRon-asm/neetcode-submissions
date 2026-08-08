class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #for merging intervals:
        #first we sort the intervals by starting index

        intervals.sort(key=lambda x: x[0])
        #the function should always return something
        #even if there's nothing in the input
        output = [intervals[0]]
        
        for item in intervals: #for each item in the sorted array
            lastEnd = output[-1][1] #-> lastEnd is the end value of the last item in the input

            if item[0] <= lastEnd: #if this item's start point is less than or equal to the endpoint (if it's overlapping)
                output[-1][1] = max(lastEnd, item[1]) # merge the intervals, by making the newest endpoint the highest of the two points.
            else: # otherwise, if they're not overlapping
                output.append([item[0],item[1]]) #it gets added to the list of overlapping intervals
        return output