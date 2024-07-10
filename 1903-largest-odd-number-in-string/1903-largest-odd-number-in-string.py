class Solution:
    def largestOddNumber(self, nums: str) -> str:
        i = len(nums)-1
        
        while i>=0 and int(nums[i])%2 == 0:
                i -= 1
        
        return nums[:i+1]