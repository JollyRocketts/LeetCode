class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        
        for i in nums:
            if i == 0:
                return 0
            
            if i < 0:
                ans ^= 1
                
        if ans == 1:
            return 1
        else:
            return -1