from collections import Counter
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        l = []
        for i in roads:
            l.extend(i)
        tot = 0
        v = list(Counter(l).values())
        v.sort(reverse = True)
        for i in v:
            tot += i*n
            n -= 1
        return tot