class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","")
        s = s.lower()
        s = "".join(c for c in s if c.isalnum())
        for i in range(0,len(s)//2):
            if s[i] != s[len(s)-i-1]:
                return False
        return True
                