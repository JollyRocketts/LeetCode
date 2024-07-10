class Solution:
    def myAtoi(self, s: str) -> int:
        
        s = s.lstrip()
        
        if s == "":
            return 0
            
        i = 0
        ans = ""
        flag = False
        
        if s[0] == "-":
            flag = True
            i += 1
        
        if s[0] == "+":
            i += 1
            
        while i < len(s) and s[i].isdigit():
            ans += s[i]
            i += 1
            
        if len(ans) == 0:
            return 0
        
        if flag == True:
            ans = -1 * int(ans)
            
        if int(ans) > (2**31 -1):
            ans = 2**31 - 1
            
        if int(ans) < -2**31:
            ans = -2**31
            
        return int(ans)