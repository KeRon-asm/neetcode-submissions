class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checked = []
        for x in nums:
            if x in checked:
                return True
            else:
                checked.append(x)
        return False