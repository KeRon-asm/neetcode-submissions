class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #DON'T HAVE TO CONVERT TO NUMBERS!
        res = {} # k,v = alphabet_list, list of strings

        for word in strs: # for each word
            alphabet_list = [0] * 26 #create an alphabet list
            for letter in word: #for each letter in that word
                alphabet_list[ord(letter) - ord('a')] += 1 #increment the corresponding value
            key = tuple(alphabet_list)
            if key not in res:
                res[key] = []
            res[key].append(word)

        return list(res.values())