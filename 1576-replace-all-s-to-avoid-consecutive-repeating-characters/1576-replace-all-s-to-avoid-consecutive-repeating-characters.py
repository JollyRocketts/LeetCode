class Solution:
    def modifyString(self, s: str) -> str:
        for i in range(len(s)):
            if s[i] == "?" and i != len(s) - 1:
                j = 97
                while ord(s[i-1]) == j or ord(s[i+1]) == j:
                    j += 1
                s = s.replace("?", chr(j), 1)
            elif s[i] == "?" and i == len(s) - 1:
                j = 97
                while ord(s[i-1]) == j:
                    j += 1
                s = s.replace("?", chr(j), 1)
        return s