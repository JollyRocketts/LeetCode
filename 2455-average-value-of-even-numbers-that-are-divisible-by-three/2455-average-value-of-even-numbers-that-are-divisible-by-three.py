class Solution:
    def averageValue(self, nums: List[int]) -> int:
        tot = 0
        num = 0
        
        for i in nums:
            if i % 6 == 0:
                tot += i
                num += 1
                
        if num == 0:
            return 0
        
        return tot//num