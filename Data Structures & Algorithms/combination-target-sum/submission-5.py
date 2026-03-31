class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans,t=[],[]
        def dfs(i, curr_sum):
            if curr_sum==target:
                ans.append(t.copy())
                return
            if curr_sum>target or i>=len(nums):
                return
            
            dfs(i+1, curr_sum)
            t.append(nums[i])
            dfs(i, curr_sum+nums[i])
            t.pop()
            
        dfs(0,0)
        return ans
