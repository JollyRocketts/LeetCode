class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        if s == "":
            return 1
        
        l = 0
        
#         while l < len(s) and s[l] == "1":
#             l += 1
        
        maxm = 0
        
        while l < len(s):
            
            if s[l] == "1":
                l += 1
                continue
            
            r = l+1
            # zero = True
            
            while r < len(s) and s[r] != "1":
                r += 1
            
            temp = r-l
            # print(l)
            
            while r < len(s) and s[r] != "0":
                r += 1
                if r-l == 2*temp:
                    maxm = max(maxm, temp*2)
                    break
            
            # print(r)
            # print(r-l)
            
                
            l += 1
            #print(l)
            
        return maxm