

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        if s[0] == ')' or s[0] == '}' or s[0] == ']':
            return False 

        for i in s:
            if i == ')' or i == '}' or i == ']':
                if len(stack)==0:
                    return False
                elif stack[-1] == pairs[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if len(stack) > 0:
            return False
        return True