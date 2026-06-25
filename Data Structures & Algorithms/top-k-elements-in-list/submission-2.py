class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frq = {}

        for key in nums:
            if key in frq:
                frq[key] +=1
            else:
                frq[key] = 1
        sorted_keys = sorted(frq, key=frq.get, reverse=True)

        return sorted_keys[:k]