from itertools import combinations
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        curr = 1
        idx = 0
        res = 0
        while curr <= n:
            if idx < len(nums) and nums[idx] <= curr:
                curr += nums[idx]
                idx += 1
            else:
                res += 1
                curr *= 2
        return res