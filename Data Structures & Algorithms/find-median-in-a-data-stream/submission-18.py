class MedianFinder:

    def __init__(self):
        self.s=[]
        self.t=[]

    def addNum(self, num: int) -> None:
        s=self.s
        t=self.t
        heapq.heappush(s, num*-1)
        
        if t and s[0]*-1>t[0]:
            heapq.heappush(t,heapq.heappop(s)*-1)
        if len(s)-len(t)>1:
            heapq.heappush(t,heapq.heappop(s)*-1)
        if len(t)-len(s)>1:
            heapq.heappush(s,heapq.heappop(t)*-1)

        

    def findMedian(self) -> float:
        s=self.s
        t=self.t
        if len(s)>len(t):
            return s[0]*-1
        elif len(s)<len(t):
            return t[0]
        else:
            return (s[0]*-1+t[0])/2
        