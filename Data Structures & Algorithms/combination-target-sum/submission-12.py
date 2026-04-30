class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        def sub(i, curr_sum,t):
            nonlocal ans
            if i>len(nums)-1 or curr_sum>target:
                return
            if curr_sum==target:
                ans.append(t.copy())
                return
            sub(i+1, curr_sum,t)
            t.append(nums[i])
            sub(i, curr_sum+nums[i],t)
            t.pop()
        sub(0,0,[])
        return ans