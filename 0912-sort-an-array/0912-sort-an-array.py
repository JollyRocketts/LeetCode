from random import randint

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def s(l, r):
            if l>=r:
                return
            
            piv = nums[random.randint(l, r)]
            less = l-1
            more = r+1
            k = l
            
            while k<more:
                if nums[k]<piv:
                    less += 1
                    nums[less], nums[k] = nums[k], nums[less]
                    k += 1
                elif nums[k]>piv:
                    more -= 1
                    nums[more], nums[k] = nums[k], nums[more]
                else:
                    k += 1
            
            s(l, less)
            s(more, r)
            
        s(0, len(nums)-1)
        
        return nums