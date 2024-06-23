from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        return max(Counter(Counter(nums).values()))*Counter(Counter(nums).values())[max(Counter(Counter(nums).values()))]