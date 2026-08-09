class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans=[intervals[0]]
        for i,j in intervals[1:]:
            l=ans[-1][1]
            if i<=l:
                ans[-1][1]=max(l,j)
            else:
                ans.append([i,j])
        return ans

