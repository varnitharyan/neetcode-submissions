from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*(len(nums))
        pre=1
        pos=1
        for i in range(len(nums)):
            res[i]=pre
            pre*=nums[i]
        for j in range(len(nums)-1,-1,-1):
            res[j]*=pos
            pos*=nums[j]
        return res