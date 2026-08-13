class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #sort, insert, and merge

        #empty edge case
        if not intervals:
            return [newInterval]

        #Sort
        #intervals.sort(key=lambda x: x[0])

        #Insert
        inserted = False
        for pos, item in enumerate(intervals):
            if newInterval[0] < item[0]:
                intervals.insert(pos, newInterval)
                inserted = True
                break
        
        #if not inserted, doesn't overlap, add to end
        if inserted == False:
            intervals.append(newInterval)

        #Merge
        output = [intervals[0]]
        for item in intervals[1::]:
            previous_interval_endpoint = output[-1][1]

            if item[0] <= previous_interval_endpoint:
                output[-1][1] = max(previous_interval_endpoint, item[1])
            else:
                output.append(item)
        return output
