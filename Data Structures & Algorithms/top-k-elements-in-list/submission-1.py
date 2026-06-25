
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frq = {}
        #Store values in a dictionary
        #return most counted values in the dictionary
        for key in nums: #for every element in the list
            #If the element is in dict, increment it
            if key in frq:
                frq[key] = frq[key]+1
            else: #If not, add it
                frq[key] = 1
            #return k highest values in dictionary
            
        sorted_keys = sorted(frq, key=frq.get,reverse = True)
        return sorted_keys[:k]