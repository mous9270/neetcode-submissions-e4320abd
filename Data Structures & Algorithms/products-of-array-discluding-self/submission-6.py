class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=[1 for i in range(len(nums))]
        q=[1 for i in range(len(nums))]
        ans=[1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            p[i]=p[i-1]*nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            q[i]=q[i+1]*nums[i+1]
        for i in range(len(q)):
            ans[i]=p[i]*q[i]
        return ans