class MedianFinder:

    def __init__(self):
        self.small=[]
        self.large=[]
         

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        s=self.small
        l=self.large
        if l and  s[0]*-1>l[0]:
            heapq.heappush(self.large, heapq.heappop(self.small)*-1)
        if len(s)-len(l)>1:
            heapq.heappush(self.large, heapq.heappop(self.small)*-1)
        if len(l)-len(s)>1:
            heapq.heappush(self.small, heapq.heappop(self.large)*-1)
        
        
        

    def findMedian(self) -> float:
        s=self.small
        l=self.large
        if len(s)>len(l):
            return s[0]*-1
        elif len(l)>len(s):
            return l[0]
        else:
            return ((s[0]*-1)+l[0])/2
        
        