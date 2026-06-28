class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #max possible frequency is the length of the array
        #each index represents a frequency and at each index we store all numbers that appear that many times in a list
        #Afterwards, take highest possible frequencies and collect numbers until we have k of them
        counts = {}
        freq = [[] for i in range(len(nums)+1)] #make the frequency list as long as nums
        for num in nums: #for every element in nums
            counts[num] = 1 + counts.get(num,0) # count.get(x,0) provides a default value for a key if it's missing
        for num, counts in counts.items(): # for each pair in dictionary
            freq[counts].append(num) # add the element from the nums list into the freq list bucket

        result = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result