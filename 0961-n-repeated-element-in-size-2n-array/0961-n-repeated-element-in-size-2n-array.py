class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)//2
        # print(n)
        for i in range(n+1):
            # print(nums.count(nums[i]))
            if nums.count(nums[i]) == n:
                return nums[i]