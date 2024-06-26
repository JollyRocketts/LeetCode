from collections import Counter
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = Counter(nums)[0]
        for i in range(c):
            nums.remove(0)
            nums.append(0)