class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Handle the empty list edge case
        if not intervals:
            return [newInterval]
            
        inserted = False
        
        # Use enumerate to find the correct insertion position safely
        for pos, item in enumerate(intervals):
            if newInterval[0] < item[0]:
                intervals.insert(pos, newInterval)
                inserted = True
                break
        
        # If the loop finishes without inserting, it belongs at the end
        if not inserted:
            intervals.append(newInterval)
            
        # Merge all intervals
        output = [intervals[0]]
        for item in intervals[1:]:
            previous_interval_endpoint = output[-1][1]

            if item[0] <= previous_interval_endpoint:
                output[-1][1] = max(previous_interval_endpoint, item[1])
            else:
                output.append(item)
        
        return output