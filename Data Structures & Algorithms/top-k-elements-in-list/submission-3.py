class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen={}
        a=[[] for _ in range(len(nums)+1)]
        for i in nums:
            if i in seen:
                seen[i]+=1
            else:
                seen[i]=1
        for key,value in seen.items():
            a[value].append(key)
        res=[]
        for i in range(len(a)-1,0,-1):
            for num in a[i]:
                res.append(num)
                if len(res)==k:
                    return(res)