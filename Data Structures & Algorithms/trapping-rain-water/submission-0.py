class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        leftmax=[0]*len(height)
        rightmax=[0]*len(height)
        lm=0
        rm=0
        water=0
        for _ in range(len(height)):
            lm=max(lm,height[left])
            rm=max(rm,height[right])
            leftmax[left]=lm
            rightmax[right]=rm
            left+=1
            right-=1
        for i in range(len(height)):
            water+=min(leftmax[i],rightmax[i])-height[i]
        return(water)