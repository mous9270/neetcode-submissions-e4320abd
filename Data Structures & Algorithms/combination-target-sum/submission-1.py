class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(target, stack, index):
            if target==0:
                ans.append(stack.copy())
                return
            if target<0:
                return

            for i in range(index, len(nums)):
                stack.append(nums[i])
                backtrack(target-nums[i], stack, i)
                stack.pop()
        backtrack(target, [], 0)
        return ans
