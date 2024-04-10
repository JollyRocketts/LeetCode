class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        maxmm = 1
        for i in range(len(s)-1):
            l = 0
            while (i+l)!=len(s) and s[i+l] not in s[i:i+l]:
                l += 1
            if l>maxmm:
                maxmm = l
        return maxmm
