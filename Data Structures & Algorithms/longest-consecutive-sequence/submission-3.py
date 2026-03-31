class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=set(nums)
        ans=0
        for i in n:
            if i-1 not in n:
                k=i
                c=1
                while k+1 in n:
                    c+=1
                    k+=1
                ans=max(ans,c)
        return ans
