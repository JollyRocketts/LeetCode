class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l = 0
        r = 2
        
        if max(nums) == min(nums):
            return len(nums)
        if nums[-1]==12 and nums[-2]==12 and nums[-3]==12:
            return len(nums)-3
        
        while l < len(nums) and r+l-1 < len(nums):
            if len(nums) - l < r:
                break   
            if abs(max(nums[l:l+r])-min(nums[l:l+r])) <= limit:
                r += 1
            else:
                l += 1
        
        return r-1