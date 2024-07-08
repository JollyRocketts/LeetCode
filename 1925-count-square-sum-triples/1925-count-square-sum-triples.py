class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        
        for c in range(1, n+1):
            a = 1
            while a**2 <= (c**2)/2:
                if math.sqrt(c**2-a**2)%1 == 0:
                    #print(a,c)
                    count += 2
                a += 1
                
        return count