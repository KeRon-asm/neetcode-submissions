class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            "}": "{",
            ")" : "(",
            "]" : "[",
            }
        #check all items
        for char in s:
            if char in closeToOpen: #check if item is a closing bracket
                if stack and (stack[-1] == closeToOpen[char]):
                    stack.pop()
                else:
                    return False
            else: #otherwise, add to stack
                stack.append(char)
        if stack:
            return False
        if not stack:
            return True