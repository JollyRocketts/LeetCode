class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        maxm = 0
        nums.sort()
        l = 0
        r = 1
        
        while l<len(nums)-1:
            # print(l, r, len(nums))
            # print(nums[l], nums[r])
            if nums[r]-nums[l] > nums[l]:
                l += 1
                r = l+1
            else:
                maxm = max(maxm, nums[l]^nums[r])
                r += 1
                if r == len(nums):
                    l += 1
                    r = l+1
                
        return maxm
        
#         for i in range(len(nums)):
#             for j in range(i, len(nums)):
#                 if abs(nums[i]-nums[j]) <= nums[i]
                
                
                
                
                
#         if i == j no use, res will be 0
#         if diff b/w i and j exceeds min then incr i as it's too low then j = i+1