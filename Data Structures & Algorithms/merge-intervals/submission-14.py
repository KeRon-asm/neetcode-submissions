class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort
        #merge
        #expecting time complexity of O(n log n)
        
        #empty edge case
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        
        output = [intervals[0]]

        #compare intervals

        #if they overlap, merge

        #if not, append interval
        # item[0] = start
        # item[1] = end
        for item in intervals:
            previous_endpoint = output[-1][1]

            if item[0] <= previous_endpoint:
                output[-1][1] = max(item[1], previous_endpoint)
            else:
                output.append(item)
        return output