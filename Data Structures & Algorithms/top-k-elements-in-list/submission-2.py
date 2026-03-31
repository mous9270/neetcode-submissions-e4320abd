class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        t=[[] for i in range(len(nums)+1)]
        m={}
        ans=[]
        for i in nums:
            m[i]=m.get(i,0)+1
        for i in m:
            t[m[i]].append(i)
        for i in range(len(t)-1,0,-1):
            for j in t[i]:
                ans.append(j)
                if len(ans)==k:
                    return ans
