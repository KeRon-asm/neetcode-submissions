class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    # turn the letters into numbers
    # sort and compare
        if len(s) == len(t):
            s = ''.join(sorted(s))
            t = ''.join(sorted(t))
            if s == t:
                return True
            else:
                return False
        else:
            return False