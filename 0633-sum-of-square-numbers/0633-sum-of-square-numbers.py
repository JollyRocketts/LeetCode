class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int(math.sqrt(c))+1):
            if math.sqrt(c-i**2)%1 == 0.0:
                return True
        return False