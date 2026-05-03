class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashing array approach
        # Match each value in num to its index
        map = {}
        # Create for loop
        for i in range(len(nums)):
        # Complement = target - num[i]
            complement = target - nums[i]
        # Check if comp in table
            if complement in map:
                return [map[complement], i]
        # If so, return value
            else:
                map[nums[i]] = i
        # If not, add it
        return