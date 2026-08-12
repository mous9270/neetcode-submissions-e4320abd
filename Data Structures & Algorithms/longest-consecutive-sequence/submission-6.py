class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s=set(nums)
        ans=float('-inf')
        for i in nums:
            c=0
            if i-1 not in s:
                c+=1
                while i+1 in s:
                    c+=1
                    i+=1
                ans=max(ans,c)
        return ans
