from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums).values()
        return max(Counter(c))*Counter(c)[max(Counter(c))]