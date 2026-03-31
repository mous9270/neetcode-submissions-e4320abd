class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            s+=str(len(i))+"#"+i
        return s
            

    def decode(self, s: str) -> List[str]:
        ans = []
        l = 0
        while l<len(s):
            r=l
            while s[r]!="#":
                r+=1
            i = int(s[l:r])
            t = s[r+1: r+i+1]
            ans.append(t)
            l=r+i+1

        return ans
