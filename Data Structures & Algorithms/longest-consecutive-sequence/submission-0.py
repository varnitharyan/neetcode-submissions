class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        log=0
        for i in sett:
            if i-1 not in sett:
                j=i
                cur=0
                while j in sett:
                    j+=1
                    cur+=1
                if cur>log:
                    log=cur
            else:
                continue
        return log