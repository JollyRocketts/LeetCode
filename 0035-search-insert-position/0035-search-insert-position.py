class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        def binS(l, x, low, high):
            
            mid = (low+high)//2
            
            if low >= high:
                if x<=l[low]:
                    return low
                else:
                    return high+1
            
            # print(mid, x)
            
            if l[mid] == x:
                return mid
            elif l[mid] < x:
                return binS(l, x, mid+1, high)
            else:
                return binS(l, x, low, mid-1)
            
        ans = binS(nums, target, 0, len(nums)-1)
        
        return ans
            