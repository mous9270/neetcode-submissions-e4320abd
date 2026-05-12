class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==2 or len(nums)==3:
            return max(nums)
        def sub(nums):
            # if len(nums)==1:
            #     return nums[0]
            # if len(nums)==2:
            #     return max(nums[0],nums[1])
            a,b=nums[0],max(nums[0],nums[1])
            for i in range(2, len(nums)):
                t=b
                b=max(b, a+nums[i])
                a=t
            return b
        return max(sub(nums[1:]), sub(nums[:-1]))

