class Solution:
    def maxScore(self, s: str) -> int:
        
        def left(s):
            score = 0
            for i in s:
                if i == "0":
                    score += 1
            return score
        
        def right(s):
            score = 0
            for i in s:
                if i == "1":
                    score += 1
            return score
        
        ans = 0
        
        for i in range(1, len(s)):
            ans = max(ans, left(s[:i]) + right(s[i:]))
        
        return ans