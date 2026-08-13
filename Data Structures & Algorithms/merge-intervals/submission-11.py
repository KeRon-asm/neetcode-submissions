class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort the intervals
        intervals.sort(key=lambda x: x[0])

        #start the output from the first interval
        output = [intervals[0]]

        #iterate through sorted intervals
        for item in intervals:
            previous_interval_endpoint = output[-1][1]

            if item[0] <= previous_interval_endpoint:
                output[-1][1] = max(previous_interval_endpoint, item[1])
            else:
                output.append(item)
        return output