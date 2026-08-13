class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #intervals are not sorted
        #return merged, non-overlapping intervals
        #edge case
        if not intervals:
            return []
        #sort
        
        intervals.sort(key=lambda x: x[0])
        #merge/append
        
        output = [intervals[0]]
        for item in intervals[1::]:
            previous_interval_endpoint = output[-1][1]
            if item[0] <= previous_interval_endpoint:
                output[-1][1] = max(item[1],previous_interval_endpoint) #merge
            else: # append non-overlapping interval
                output.append(item)
        return output