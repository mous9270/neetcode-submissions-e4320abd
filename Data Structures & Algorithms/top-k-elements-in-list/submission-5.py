class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m={}
        ans=[[] for i in range(len(nums)+1)]
        res=[]
        for i in nums:
            m[i]=m.get(i,0)+1
        for i in m:
            ans[m[i]].append(i)
        for i in range(len(ans)-1, -1,-1):
            for j in ans[i]:
                res.append(j)
                if len(res)==k:
                    return res
        