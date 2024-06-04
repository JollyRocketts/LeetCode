from collections import defaultdict
class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        def func():
            return 0
        d = defaultdict(func)
        arr = []
        for i in range(len(nums)):
            d[nums[i]] += 1
        for i in d:
            if d[i] == 2:
                arr.append(i)
        if len(arr) == 0:
            return 0
        else:
            res = 0
            for i in arr:
                res ^= i
            return res