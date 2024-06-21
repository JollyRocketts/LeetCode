class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        z = [i for i in zip(customers,grumpy)]
        res = sum([i[0] for i in z if i[1] == 0])
        m = 0
        l = 0
        r = l + minutes
        while r<=len(grumpy):
            m = max(m, sum([i[0] for i in z[l:r] if i[1] == 1]))
            l += 1
            r += 1
        return res+m