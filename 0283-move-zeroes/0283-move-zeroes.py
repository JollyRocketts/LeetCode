from collections import Counter
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(Counter(nums)[0]):
            nums.append(0)
            nums.remove(0)