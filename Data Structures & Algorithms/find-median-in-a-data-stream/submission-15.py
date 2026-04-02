class MedianFinder:

    def __init__(self):
        self.small=[]
        self.large=[]

    def addNum(self, num: int) -> None:
        s=self.small
        l=self.large
        heapq.heappush(s, num*-1)
        if l and l[0]<s[0]*-1:
            heapq.heappush(l, heapq.heappop(s)*-1)
        if len(s)-len(l)>1:
            heapq.heappush(l, heapq.heappop(s)*-1)
        if len(l)-len(s)>1:
            heapq.heappush(s, heapq.heappop(l)*-1)

    def findMedian(self) -> float:
        s=self.small
        l=self.large
        if len(l)>len(s):
            return l[0]
        elif len(s)>len(l):
            return s[0]*-1
        else:
            return (l[0]+(s[0]*-1))/2
        
        