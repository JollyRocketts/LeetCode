class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        l = 0
        r = l+1
        count = 1
        temp = 1
        
        while l<len(s)-1:
            if r<len(s) and ord(s[r]) == ord(s[l]) + 1:
                l += 1
                r += 1
                temp += 1
            else:
                count = max(count, temp)
                l = r
                r += 1
                temp = 1
        
        return max(count, temp)