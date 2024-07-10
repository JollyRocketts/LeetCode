class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        incr = True
        decr = True
        
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                decr = False
            if nums[i] < nums[i-1]:
                incr = False
                
        return incr or decr