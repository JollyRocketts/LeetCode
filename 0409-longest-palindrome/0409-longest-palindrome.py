from collections import defaultdict
class Solution:
    def longestPalindrome(self, s: str) -> int:
        def func():
            return 0
        d = defaultdict(func)
        for i in range(len(s)):
            d[s[i]] += 1
        sum = 0
        flag = False
        if len(d) == 1:
            return len(s)
        for i in d:
            if d[i] % 2 == 0:
                sum += d[i]
            else:    
                sum += d[i] - 1
                flag = True
        if flag:
            return sum + 1
        else:
            return sum