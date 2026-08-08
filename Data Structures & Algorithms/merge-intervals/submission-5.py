class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #edge cases
        if not intervals: #if empty
            return []
        
        
        #sort the items by starting point

        intervals.sort(key=lambda x: x[0])
        #Timsort creates an automatic O(n log n) 

        output = [intervals[0]]
        for item in intervals: # check each item in the input
            lastEnd = output[-1][1]

            if item[0] <= lastEnd: #if the starting point is less than or equal to the endpoint
                output[-1][1] = max(lastEnd, item[1]) # merge, and update the last item's endpoint to be the largest of the two
                
            else: # otherwise, add it to the non-overlapping interval list
                output.append([item[0],item[1]])
        return output