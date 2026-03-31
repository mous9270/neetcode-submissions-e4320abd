class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def backtrack(r, s, si):
            if r == 0:
                ans.append(s.copy())
                return
            if r < 0:
                return
            
            for i in range(si, len(nums)):
                s.append(nums[i])
                backtrack(r - nums[i], s, i)
                s.pop()
        
        backtrack(target, [], 0)
        return ans