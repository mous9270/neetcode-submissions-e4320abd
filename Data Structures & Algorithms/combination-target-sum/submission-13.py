class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        def dfs(i,curr_sum,t):
            if i>len(nums)-1 or curr_sum>target:
                return
            if curr_sum==target:
                ans.append(t.copy())
                return
            dfs(i+1, curr_sum,t)
            t.append(nums[i])
            dfs(i,curr_sum+nums[i],t)
            t.pop()
        dfs(0,0,[])
        return ans
