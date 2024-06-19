class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
        
        def check(mid, arr, m, k):
            temp = 0
            tot = 0
            for i in arr:
                if i<=mid:
                    temp += 1
                else:
                    temp = 0
                if temp == k:
                    tot += 1
                    temp = 0
            if tot >= m:
                return True
            else:
                return False
        
        def bins(arr, l, r, m, k):
            if l == r:
                return l
            mid = (l+r)//2
            if check(mid, arr, m, k):
                return bins(arr, l, mid, m, k)
            else:
                return bins(arr, mid+1, r, m, k)
            
        return bins(bloomDay, min(bloomDay), max(bloomDay), m, k)