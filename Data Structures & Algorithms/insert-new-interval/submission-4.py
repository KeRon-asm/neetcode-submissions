class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #intervals are sorted already

        #insert the interval, then merge
        if not intervals:
            return [newInterval]
        
        inserted = False
        for pos, item in enumerate(intervals):
            if newInterval[0] < item[0]:
                intervals.insert(pos, newInterval)
                inserted = True
                break
                
            #if item not inserted, it belongs at the end
        if not inserted:
            intervals.append(newInterval)
        #now merge all intervals
        output = [intervals[0]]
        for item in intervals:
            previous_interval_endpoint = output[-1][1]

            if item[0] <= previous_interval_endpoint:
                output[-1][1] = max(previous_interval_endpoint, item[1])
            else:
                output.append(item)
        
        return output

            