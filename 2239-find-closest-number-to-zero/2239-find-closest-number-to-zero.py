class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        maxd = float('inf')
        ans = float('-inf')
        
        for i in nums:
            d = abs(0-i)
            if d < maxd:
                maxd = d
                ans = i
            elif d == maxd and i > ans:
                ans = i
        
        return ans