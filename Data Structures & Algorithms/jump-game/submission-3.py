class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==0 or len(nums)==1:
            return True
        l,r=len(nums)-1,len(nums)-2
        while r>-1:
            # if l==0:
            #     return True
            if r+nums[r]>=l:
                l=r
            r-=1    
        return True if l==0 else False
        