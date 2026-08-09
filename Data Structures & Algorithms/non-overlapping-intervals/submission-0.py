class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        p=intervals[0][1]
        ans=0
        for i,j in intervals[1:]:
            if i<p:
                ans+=1
                p=min(p,j)
            else:
                p=j
        return ans
