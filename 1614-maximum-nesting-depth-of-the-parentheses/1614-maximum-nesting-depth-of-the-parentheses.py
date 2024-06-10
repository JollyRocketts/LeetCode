class Solution:
    def maxDepth(self, s: str) -> int:
        m = 0
        l = 0
        r = 0
        for i in s:
            if i == "(":
                l += 1
            elif i == ")":
                r += 1
            m = max(l - r, m)
        return m