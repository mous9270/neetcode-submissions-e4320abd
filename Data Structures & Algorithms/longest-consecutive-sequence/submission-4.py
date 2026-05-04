class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        ans=0
        for i in s:
            c=1
            if i-1 not in s:
                k=i
                while k+1 in s:
                    c+=1
                    k+=1
                ans=max(ans,c)
        return ans