class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        m={}
        l=len(nums)
        m[0]=nums[0]
        m[1]=max(nums[:2])
        for i in range(l):
            if i not in m:
                m[i]=max(m[i-1], m[i-2]+nums[i])
        
        return m[l-1]