class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        m=[[] for i in range(len(nums)+1)]
        n={}
        for i in nums:
            n[i]=n.get(i,0)+1
        for i in n:
            m[n[i]].append(i)
        for i in range(len(m)-1,0,-1):
            for j in m[i]:
                if k>0:
                    ans.append(j)
                    k-=1
        return ans