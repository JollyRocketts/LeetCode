class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0

        #         nnums = []
        
#         for i in nums:
#             if i not in nnums:
#                 nnums.append(i)
        
#         for i in range(1,len(nnums)-1):
#             if (nnums[i-1]<nnums[i] and nnums[i+1]<nnums[i]) or (nnums[i-1]>nnums[i] and nnums[i+1]>nnums[i]):
#                 count += 1
          
    
        # for i in range(1,len(nums)-1):
        
        i = 1
        
        while i < len(nums)-1:
            l = i-1
            r = i+1
            
            while l > 0 and nums[l] == nums[i]:
                l -= 1
            while r < len(nums)-1 and nums[r] == nums[i]:
                r += 1
                
            if (nums[l]<nums[i] and nums[r]<nums[i]) or (nums[l]>nums[i] and nums[r]>nums[i]):
                count += 1
            
            i = r
        
        return count