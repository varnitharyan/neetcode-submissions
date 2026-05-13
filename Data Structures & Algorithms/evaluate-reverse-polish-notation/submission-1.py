class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operand = []
        ans=0
        for i in tokens:
            if i not in {"+", "-", "*", "/"}:
                operand.append(int(i)   )
            else:
                right = operand.pop()
                left = operand.pop()
                if i == "+":
                    ans = int(left) + int(right)
                elif i == "-":
                    ans = int(left) - int(right)
                elif i == "*":
                    ans = int(left) * int(right)
                else:
                    ans = int(int(left) / int(right))
                operand.append(ans)
        return(operand[-1])