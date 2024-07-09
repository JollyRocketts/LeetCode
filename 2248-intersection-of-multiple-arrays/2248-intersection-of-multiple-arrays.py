class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        temp = set(nums[0])
        
        for i in range(1,len(nums)):
            temp = temp.intersection(set(nums[i]))
            
        return sorted(list(temp))