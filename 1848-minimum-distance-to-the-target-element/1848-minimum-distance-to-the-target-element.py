class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        l = start-1
        r = start
        
        while l >= 0 or r < len(nums):
            if r < len(nums) and nums[r] == target:
                return abs(r-start)
            else:
                r += 1
                
            if l >= 0 and nums[l] == target:
                return abs(l-start)
            else:
                l -= 1
            
            