from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        prod = 1
        
        for i in nums:
            if i == 0:
                zero_count += 1
            else:
                prod *= i
        
        for j in range(len(nums)):
            if zero_count > 1:
                nums[j] = 0
            elif zero_count == 1:
                if nums[j] == 0:
                    nums[j] = prod
                else:
                    nums[j] = 0
            else:
                nums[j] = prod // nums[j]
        
        return nums