class MedianFinder:

    def __init__(self):
        self.val=[]

    def addNum(self, num: int) -> None:
        self.val.append(num)
        self.val.sort()
        

    def findMedian(self) -> float:
        m=len(self.val)//2
        if len(self.val)%2==0:
            return (self.val[m-1]+self.val[m])/2
        else:
            return self.val[m]
        
        