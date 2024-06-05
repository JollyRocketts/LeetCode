class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        tsum = sum(arr)
        if tsum%3 != 0:
            return False
        r = len(arr)-2
        l = 1
        lsum = arr[0]
        rsum = arr[-1]
        av = tsum//3
        while l <= r:
            if l<r and lsum != av:
                lsum += arr[l]
                l += 1
            if l<r and rsum != av:
                rsum += arr[r]
                r -= 1
            if lsum == rsum == av:
                return True
            if l == r:
                return False
        return False