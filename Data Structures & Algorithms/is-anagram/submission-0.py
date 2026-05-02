class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    # turn the letters into numbers
    # sort and compare
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        if s == t:
            return True
        else:
            return False