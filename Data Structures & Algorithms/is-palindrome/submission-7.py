class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        t=""
        for i in s:
            if i.isalnum():
                t+=i.lower()
        return t==t[::-1]