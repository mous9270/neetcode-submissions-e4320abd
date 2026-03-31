class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        def back(curr_sum, i, t):
            nonlocal ans
            if i>len(nums)-1:
                return
            if curr_sum>target:
                return
            if curr_sum==target:
                ans.append(t.copy())
                return
            t.append(nums[i])
            back(curr_sum+nums[i], i, t)
            t.pop()
            back(curr_sum, i+1, t)
        back(0,0,[])
        return ans
            