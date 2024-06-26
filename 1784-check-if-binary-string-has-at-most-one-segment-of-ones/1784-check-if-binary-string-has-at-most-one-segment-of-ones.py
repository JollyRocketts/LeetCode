from collections import Counter
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        c = Counter(s)['1']
        for i in s:
            if i == '1':
                c -= 1
            elif c > 0:
                return False
            if c == 0:
                return True