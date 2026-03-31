class Solution:
    def isValid(self, s: str) -> bool:
        m={'{':'}', '[':']', '(':')'}
        n={}
        for i in m:
            n[m[i]]=i
        if len(s)==0:
            return True
        if len(s)==1:
            return False
        t=[]
        for i in range(len(s)):
            if s[i] in m:
                t.append(s[i])
            else:
                if t and t.pop()==n[s[i]]:
                    continue
                else:
                    return False
        return True if len(t)==0 else False
