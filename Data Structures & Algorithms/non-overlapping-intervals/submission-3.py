class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ivs=sorted(intervals, key=lambda i:i[0])
        ans=0
        t=ivs[0][1]
        for j in range(1,len(ivs)):
            i=ivs[j]
            if i[0]<t:
                ans+=1
                t=min(t,i[1])
            else:
                t=max(t,i[1])
        return ans
