class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans=[[] for i in range(len(nums)+1)]
        m={}
        t=[]
        for i in nums:
            m[i]=m.get(i,0)+1
        for i in m:
            ans[m[i]].append(i)
        for i in range(len(ans)-1, 0, -1):
            for j in ans[i]:
                ans[0].append(j)
                if len(ans[0])==k:
                    return ans[0]
