class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #intervals are sorted already
        #intuition is insert, merge
        if not intervals:
            return [newInterval]

        #insert
        inserted = False
        for pos, item in enumerate(intervals):
            if item[0] > newInterval[0]:
                intervals.insert(pos, newInterval)
                inserted = True
                break

        if inserted == False:
            intervals.append(newInterval)
        #merge logic

        output = [intervals[0]]
        for item in intervals[1::]:
            previous_end = output[-1][1]
            
            if item[0] <= previous_end:
                output[-1][1] = max(item[1],previous_end)
            else:
                output.append(item)

        return output