class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]

        def dfs(target, ix, s):
            if target==0:
                ans.append(s.copy())
                return
            if target<0:
                return
            for i in range(ix, len(nums)):
                s.append(nums[i])
                dfs(target-nums[i], i, s)
                s.pop()

        dfs(target, 0, [])
        return ans