class MedianFinder:

    def __init__(self):
        self.val=[]

    def addNum(self, num: int) -> None:
        self.val.append(num)
        self.val.sort()

    def findMedian(self) -> float:
        if len(self.val)%2==0:
            m=len(self.val)//2
            return (self.val[m]+self.val[m-1])/2
        else:
            m=len(self.val)//2
            return self.val[m]
        
        
        