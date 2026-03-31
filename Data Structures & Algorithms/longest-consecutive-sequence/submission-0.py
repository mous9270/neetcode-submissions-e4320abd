class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        ans=0
        for i in range(len(nums)):
            l=1
            k=nums[i]
            while k+1 in s:
                l+=1
                k+=1
            if ans<l:
                ans=l

        return ans

