class Solution:
    def checkString(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        
        while l<r:
            if s[l] == "b" and s[r] == "a":
                return False
            if s[l] == "a":
                l += 1
            if s[r] == "b":
                r -= 1
            
        return True