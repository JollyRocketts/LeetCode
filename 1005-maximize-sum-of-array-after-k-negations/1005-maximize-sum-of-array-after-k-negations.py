class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        
        temp = []
        
        for i in range(len(nums)):
            if nums[i] < 0:
                temp.append(nums[i])
        
        
        while k > 0 and temp != []:
            k -= 1
            nums.remove(min(temp))
            nums.append(0-min(temp))
            temp.remove(min(temp))
        
        if k%2 == 0:
            return sum(nums)
        
#         tot = 0
        
#         for i in range(len(nums)):
#             if i%2 == 0:
#                 tot += i
                
#         k -= tot
        
        else:
            return sum(nums) - 2*min(nums)