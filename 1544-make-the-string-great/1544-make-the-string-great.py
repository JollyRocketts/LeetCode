class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        ans = ""
        flag = False
        
        while i<(len(s)-1):
            if (s[i].isupper() and s[i+1].islower() and s[i+1].upper() == s[i]) or (s[i+1].isupper() and s[i].islower() and s[i].upper() == s[i+1]):
                flag = True
                i += 2
            else:
                ans += s[i]
                i += 1
        
        if i == len(s)-1:
            ans += s[-1]
        # print(ans)
        
        if flag == False:
            return ans
        else:
            return self.makeGood(ans)
            