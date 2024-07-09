class Solution:
    def minimumSum(self, num: int) -> int:
        tot = 0
        a = []
        for i in str(num):
            a.append(int(i))
        a.sort()
        
        return a[3]+a[2]+a[1]*10+a[0]*10