class Solution:
    def modifyString(self, s: str) -> str:
        for i in range(len(s)):
            if s[i] == "?" and i != len(s) - 1 and i != 0:
                j = 97
                while ord(s[i-1]) == j or ord(s[i+1]) == j:
                    j += 1
                s = s.replace("?", chr(j), 1)
            elif i == len(s) - 1 and s[i] == "?" :
                j = 97
                while ord(s[i-1]) == j:
                    j += 1
                s = s.replace("?", chr(j), 1)
            elif i == 0 and s[i] == "?" :
                j = 97
                while ord(s[i+1]) == j:
                    j += 1
                s = s.replace("?", chr(j), 1)
        return s