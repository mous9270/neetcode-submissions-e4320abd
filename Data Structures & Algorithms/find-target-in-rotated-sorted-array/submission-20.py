class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        if len(nums)==1:
            return 0 if nums[0]==target else -1

        while l<r:
            m=(r+l)//2
            for i in [l,r,m]:
                if nums[i]==target:
                    return i
            if nums[l]<=nums[m]:
                if nums[l]<=target<=nums[m]:
                    r=m-1
                else:
                    l=m+1
            if nums[m]<=nums[r]:
                if nums[r]>=target>=nums[m]:
                    l=m+1
                else:
                    r=m-1  
            
        return m if nums[m]==target else -1
