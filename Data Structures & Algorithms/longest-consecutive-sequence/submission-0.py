class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #the longest consecutive sequence has to be at most largest_num - smallest
        result = 0
        new_nums = set(nums)
        largest = 0
        for num in new_nums:
            
            if num - 1 not in new_nums:
                largest+=1
                while num+1 in new_nums:
                    largest+=1
                    num+=1
            if largest > result:
                result = largest
            largest = 0
        return result
