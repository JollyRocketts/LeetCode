class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        p = [0]*(len(nums)+1)
        p[0] = 1
        
        tot = 0
        temp = 0
        
        for i in range(len(nums)):
            temp += nums[i]%2
            if temp >= k:
                tot += p[temp-k]
            p[temp] += 1
        
        return tot