class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        ms,mt={},{}
        for i in s:
            ms[i]=ms.get(i,0)+1
        for i in t:
            mt[i]=mt.get(i,0)+1
        return ms==mt
        