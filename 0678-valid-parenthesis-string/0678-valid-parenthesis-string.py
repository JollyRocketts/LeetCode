class Solution:
    def checkValidString(self, s: str) -> bool:
        l = 0
        r = 0
        for i in range(len(s)):
            if s[i] == "(":
                l += 1
                r += 1
            elif s[i] == ")":
                l -= 1
                r -= 1
                if r<0:
                    return False
            elif s[i] == "*":
                l -= 1
                r += 1
            if l<0:
                l = 0
        if l == 0:
            return True
        else:
            return False