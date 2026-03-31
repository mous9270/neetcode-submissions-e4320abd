class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=""
        for i in s:
            if i.isalnum():
                if i.isalpha():
                    t+=i.lower()
                else:
                    t+=i
            
        return t==t[::-1]
        