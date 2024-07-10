class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        l = 0
        # r = len(nums)-1
        
        while l<len(nums):
            if sum(nums[:l]) == sum(nums[l+1:]):
                return l
            else:
                l += 1
            
        return -1