class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
#         count = 1
#         incr = False
#         decr = False
#         temp = 1
        
#         for i in range(1, len(nums)):
#             print(temp)
#             if nums[i]>nums[i-1] and decr == False:
#                 incr = True
#                 temp += 1
#                 continue
#             else:
#                 incr = False
#                 count = max(count, temp)
                
#             if nums[i]<nums[i-1] and incr == False:
#                 temp += 1
#                 decr = True
#             else:
#                 decr = False
            
#             count = max(count, temp)
#             temp = 1
            
#         return max(count, temp)


        l = 0
        r = l+1
        count = 1
        temp = 1
        
        while l<len(nums)-1 and r<len(nums):
            if nums[r]>nums[l]:
                # print(temp)
                temp += 1
                l += 1
                r += 1
            else:
                count = max(count, temp)
                temp = 1
                l = r
                r += 1
                
        count = max(count, temp)
        # print(count)
        l = 0
        r = l+1
        count2 = 1
        temp = 1
        
        while l<len(nums)-1 and r<len(nums):
            if nums[r]<nums[l]:
                temp += 1
                l += 1
                r += 1
            else:
                count = max(count, temp)
                temp = 1
                l = r
                r += 1
                
        count2 = max(temp, count2)
        # print(count2)
        return max(count, count2)