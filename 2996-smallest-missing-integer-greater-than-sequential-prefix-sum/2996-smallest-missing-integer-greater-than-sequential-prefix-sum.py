class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        sum = nums[0]
        if len(nums) == 1:
            return sum + 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] + 1:
                sum += nums[i]
            else:
                break
            
        while True:
            if sum not in nums:
                return sum
            sum += 1