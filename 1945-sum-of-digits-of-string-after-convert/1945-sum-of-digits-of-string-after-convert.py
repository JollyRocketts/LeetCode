class Solution:
    def getLucky(self, s: str, k: int) -> int:
        tot = 0
        temp = ""
        
        for i in s:
            temp += str(ord(i)-96)
        
        for i in temp:
            tot += int(i)
        
        k -= 1
        
        while k != 0:
            temp = str(tot)
            tot = 0
            
            for i in temp:
                tot += int(i)
            
            k -= 1
            
        return tot