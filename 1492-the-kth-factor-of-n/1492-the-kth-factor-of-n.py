class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        count = 1
        i = 2
        
        while count < k:
            if i > n:
                return -1
            
            if n%i == 0:
                count += 1
            
            i += 1
        
        return i-1