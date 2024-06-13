class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        res = 0
        temp = 0
        for i in moves:
            if i == "L":
                res -= 1
            elif i == "R":
                res += 1
            else:
                temp += 1
        return abs(res) + temp