class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_water=0
        left=0
        right = len(heights)-1
        while left<right:
            water=(right-left)*min(heights[left],heights[right])
            max_water=max(water,max_water)
            if heights[left]>heights[right]:
                right-=1
            else:
                left+=1
        return(max_water)