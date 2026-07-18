class Solution:

    def encode(self, strs: List[str]) -> str:
        res = "" #encoded string is initialized 
        for s in strs: # for element in list
            res += str(len(s)) + "*" + s # add the length of the input, + a delimiter, and then the string
        return res # return a string with the length of each input + a delimiter, followed by a string

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s): # keep track of position with j
            j = i
            while s[j] != '*': # while we don't have a delimiter
                j+=1 # move forward
            length = int(s[i:j]) # when we find a delimiter, convert the length to an integer
            i = j+1 # our newest starting position is now after this word in the encoding 
            j = i + length # j is now at the end of the current word
            res.append(s[i:j]) # add the word to the list
            i = j # ensure our new starting point is at the end of this word
        return res