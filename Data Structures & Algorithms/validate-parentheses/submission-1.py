class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==0 or len(s)==1:
            return False
        t=[]
        m={'{':'}', '[':']', '(':')'}
        n={'}':'{', ']':'[', ')':'('}
        
        for i in range(len(s)):
            if s[i] in m:
                t.append(s[i])
            else:
                if t and n[s[i]]==t[-1]:
                    t.pop()
                else:
                    return False
        return True if len(t)==0 else False
