class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        def sub(i, t, s):
            if t==0:
                ans.append(s.copy())
                return
            if t<0:
                return
            for j in range(i, len(nums)):
                s.append(nums[j])
                sub(j, t-nums[j], s)
                s.pop()
        sub(0, target, [])
        return ans