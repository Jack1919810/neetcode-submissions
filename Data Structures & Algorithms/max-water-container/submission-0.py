class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        area=0
        while(left<right):
            fh=max(heights[left], heights[right])
            sh=min(heights[left], heights[right])
            if sh*(right-left)>=area:
                area=sh*(right-left)
            if heights[left]>heights[right]:
                right-=1
            else:
                left+=1
        return area
                
            