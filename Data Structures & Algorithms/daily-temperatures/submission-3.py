class Solution:
        def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
            ans = [0] * len(temperatures)
            stack = []
            for i,j in enumerate(temperatures):
                while stack and temperatures[stack[-1]]<j:
                    a = stack.pop()
                    ans[a]=i-a
                stack.append(i)
                    
            return(ans)                                                                                                                                                                  