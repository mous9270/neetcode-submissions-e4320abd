class Solution:
    def rob(self, nums: List[int]) -> int:
        ans=[]
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0],nums[1])
        ans.append(nums[0])
        ans.append(max(nums[0],nums[1]))
        for i in range(2, len(nums)):
            ans.append(max(ans[-1], ans[-2]+nums[i]))
        return ans[-1]
      