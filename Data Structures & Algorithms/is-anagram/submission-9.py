class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ms={}
        mt={}
        if len(s)!=len(t):
            return False
        for i in s:
            ms[i]=ms.get(i,0)+1
        for i in t:
            mt[i]=mt.get(i,0)+1
        for i in ms:
            if i not in mt or ms[i]!=mt[i]:
                return False
        return True