class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        l = len(nums)
        for i in range(len(nums)):
            if nums[i-l] == val:
                nums.pop(i-l)
                k += 1
        return l-k