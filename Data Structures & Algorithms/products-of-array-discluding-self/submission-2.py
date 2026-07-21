class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        # res stores 1 in every position
        prefix = 1
        #pass thru array
        #for each index i, set res[i] = prefix
        #then, update prefix to *= nums[i]
        #proceeding, each element in nums will have the product of previous elements stored
        postfix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
