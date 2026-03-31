class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        def dfs(ix, target, s):
            if target==0:
                ans.append(s.copy())
                return
            if target<0:
                return
            for i in range(ix, len(nums)):
                s.append(nums[i])
                dfs(i, target-nums[i], s)
                s.pop() 
            
            
        dfs(0, target, [])
        return ans
