class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        g = 0
        n = 0
        for i in numsDivide:
            g = math.gcd(g,i)
        nums.sort()
        for i in nums:
            if g % i == 0:
                return n
            else:
                n += 1
        return -1