class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans,t=[],[]
        def bt(i, curr_sum):
            if curr_sum==target:
                ans.append(t.copy())
                return
            if i>=len(nums) or curr_sum>target:
                return
            bt(i+1, curr_sum)
            t.append(nums[i])
            bt(i, curr_sum+nums[i])
            t.pop()
            
        bt(0,0)
        return ans