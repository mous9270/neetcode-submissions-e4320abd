class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        def dfs(curr_sum, i, t):
            nonlocal ans
            if curr_sum==target:
                ans.append(t.copy())
                return
            if i>len(nums)-1 or curr_sum>target:
                return
            dfs(curr_sum, i+1, t)
            t.append(nums[i])
            dfs(curr_sum+nums[i], i, t)
            t.pop()
        dfs(0, 0, [])
        return ans

