class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #create 2 lists, increment each index corresponding to the letter
        s_list = [0]*26
        t_list = [0]*26
        for letter in s:
            s_list[ord(letter)%26] +=1
        for letter in t:
            t_list[ord(letter)%26] +=1
        if s_list == t_list:
            return True
        else:
            return False