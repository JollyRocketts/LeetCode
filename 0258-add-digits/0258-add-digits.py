class Solution:
    def addDigits(self, num: int) -> int:
        tot = 0
        
        for i in str(num):
            tot += int(i)
        
        # print(tot)
        # print(len(str(tot)))
        if len(str(tot)) == 1:
            return tot
        else:
            tot = self.addDigits(tot)
            return tot