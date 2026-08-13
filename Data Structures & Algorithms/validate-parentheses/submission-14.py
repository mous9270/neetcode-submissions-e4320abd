class Solution:
    def isValid(self, s: str) -> bool:
        t=[]
        m={"(":")", "[":"]", "{":"}"}
        n={}
        for i in m:
            n[m[i]]=i
        if not s:
            return True
        if len(s)==1:
            return False
        if s[0] in n:
            return False
        for i in range(len(s)):
            if s[i] in m:
                t.append(s[i])
            else:
                # k=t.pop()
                if not t or t.pop()!=n[s[i]]:
                    return False
        return True if len(t)==0 else False
