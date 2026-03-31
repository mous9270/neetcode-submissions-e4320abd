class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            s+=str(len(i))+"#"+i
        return s

    def decode(self, s: str) -> List[str]:
        ans=[]
        l,r=0,0
        while r<len(s):
            while s[r]!="#":
                r+=1
            t=int(s[l:r])
            ans.append(s[r+1:r+t+1])
            l=r+t+1
            r=l
        return ans
