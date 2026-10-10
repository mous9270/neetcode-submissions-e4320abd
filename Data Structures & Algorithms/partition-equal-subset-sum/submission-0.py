class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s=sum(nums)
        if s%2!=0:
            return False
        target=s//2
        def dfs(val, i):
            if val==target:
                return True
            if i>len(nums)-1 or val>target:
                return False
            return dfs(val+nums[i],i+1) or dfs(val,i+1)
            
        return dfs(0,0)
