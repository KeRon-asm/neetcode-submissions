class Solution:
    def isValid(self, s: str) -> bool:
        #every open bracket is closed by the same bracket.
        #Open brackets are closed in the correct order
        # Every close bracket has a corresponding open bracket of the same type
        stack = []
        closeToOpen = {
            "}":"{",
            "]":"[",
            ")": "("
            }

        for char in s: # For every character in string
            if char in closeToOpen: #check if it's a closed bracket
                if stack and stack[-1] == closeToOpen[char]: # check if the item on top is an open bracket and there's an item in the stack
                    stack.pop() #If so, pop
                else: #If not, string is invalid
                    return False
            else: #If it's not, add it to the stack
                stack.append(char)
        if stack: #If the stack has items, it's invalid
            return False
        else: #If not, it's valid
            return True
                