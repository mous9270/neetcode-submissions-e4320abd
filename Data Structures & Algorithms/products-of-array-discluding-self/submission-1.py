class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=[1 for i in range(len(nums))]
        n=[1 for i in range(len(nums))]
        ans=[]
        for i in range(1, len(nums)):
            p[i]=nums[i-1]*p[i-1]
        for i in range(len(nums)-2, -1, -1):
            n[i]=nums[i+1]*n[i+1]
        for i in range(len(p)):
            ans.append(p[i]*n[i])
        return ans