class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ans = [0]* len(temperatures)



        for i in range(len(temperatures)):
            count=0
            for j in range(i,len(temperatures)):
                if temperatures[j]>temperatures[i]:
                    ans[i]=count
                    break
                else:
                    count+=1
                    
        return(ans)
            