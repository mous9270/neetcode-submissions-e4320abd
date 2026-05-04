class Solution:
    def maxArea(self, heights: List[int]) -> int:
        h=heights
        l,r=0,len(heights)-1
        ans=0
        while l<r:
            
            v=(min(h[l],h[r]))*(r-l)
            ans=max(ans,v)
            if h[l]<h[r]:
                l+=1
            else:
                r-=1
        return ans


