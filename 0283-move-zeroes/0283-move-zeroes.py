#from collections import Counter
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(Counter(nums)[0]):
        #     nums.remove(0)
        #     nums.append(0)
        i = 0
        j = 0
        
        while j < len(nums) and i<len(nums):
            if nums[i] == 0:
                nums.append(0)
                nums.pop(i)
                j += 1
            else:    
                i += 1