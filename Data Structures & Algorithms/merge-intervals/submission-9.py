class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort intervals by starting point
        intervals.sort(key=lambda x: x[0])
        
        if intervals:
            output = [intervals[0]] # output will always return an item, so long as there is one
        else:
            return []

        for item in intervals:
            previousEndpoint = output[-1][1] # the end of the last interval in the output
          
            if item[0] <= previousEndpoint:
                #if the starting point of the current item is greater than the endpoint of the previous item, merge
                output[-1][1] = max(item[1],previousEndpoint) # the endpoint becomes the larger of the two
            else: # if they aren't overlapping, add the item to the output
                output.append([item[0], item[1]])
        return output
                 
            
