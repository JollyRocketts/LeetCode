import numpy as np
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort();
        a = 1
        part = (position[-1] + position[0])//(m-1)
        res = 0
        
        def check(position, m, n):
            ini = position[0]
            tot = 1
            for i in range(len(position)):
                if position[i] - ini >= n:
                    tot += 1
                    ini = position[i]
                if tot == m:
                    return True
            return False
        
        while a<=part:
            mid = a + (part-a)//2
            if check(position, m, mid):
                res = mid
                a = mid + 1
            else:
                part = mid - 1
        
        return res