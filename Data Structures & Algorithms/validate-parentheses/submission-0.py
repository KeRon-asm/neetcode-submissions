class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "]" : "[", "}" : "{"}

        for char in s: # for every character in the string
            if char in closeToOpen: #if character is a closing bracket
                if stack and stack[-1] == closeToOpen[char]: #check if stack is empty. if not, check if last item is open
                    stack.pop() # if it is, pop
                else:
                    return False #if not, invalid parenthesis
            else:
                stack.append(char) #if not a closing bracket, add it to the stack

        return True if not stack else False #If the stack is empty, the string was valid.

        #There should be no closing brackets in the stack, that's why we flip the dictionary. Close to open, instead of 
        #open to close, because if a closing bracket is not on top of an open bracket,, invalid