class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        m = {}
        for i in nums:
            if i in m:
                return True
            else:
                m[i]=0
        return False
         