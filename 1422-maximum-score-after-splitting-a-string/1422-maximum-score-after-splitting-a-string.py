class Solution:
    def maxScore(self, s: str) -> int:
        
        z = 0
        o = 0
        
        ans = float('-inf')
        
        for i in s:
            if i == "1":
                o += 1
        
        for i in s[:-1]:
            if i == "0":
                z += 1
            else:
                o -= 1
                
            ans = max(ans, z + o)
        
        return ans
        
#         def left(s):
#             score = 0
#             for i in s:
#                 if i == "0":
#                     score += 1
#             return score
        
#         def right(s):
#             score = 0
#             for i in s:
#                 if i == "1":
#                     score += 1
#             return score
        
#         ans = 0
        
#         for i in range(1, len(s)):
#             ans = max(ans, left(s[:i]) + right(s[i:]))
        
#         return ans