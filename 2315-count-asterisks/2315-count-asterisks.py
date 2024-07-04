class Solution:
    def countAsterisks(self, s: str) -> int:
        tot = 0
        flag = 1
        for i in s:
            if i == "|":
                flag ^= 1
            if flag == 1 and i == "*":
                tot += 1
        
        return tot