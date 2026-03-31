class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[]
        p=[1 for i in range(len(nums)+1)]
        n=[1 for i in range(len(nums)+1)]
        for i in range(1,len(nums)):
            p[i]=p[i-1]*nums[i-1]
        for i in range(len(nums)-2, -1,-1):
            n[i]=n[i+1]*nums[i+1]
        for i in range(len(nums)):
            ans.append(p[i]*n[i])
        return ans
        
