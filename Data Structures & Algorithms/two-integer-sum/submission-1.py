class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashing array approach
        # only one valid solution exists, so no need to handle that edge case
        # sort items
        seen = {}
        for i, item in enumerate(nums): # for every item in input
            diff = target - item
            if diff in seen:
                return [seen[diff], i]  
            seen[item] = i