#from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
#         for i in permutations(nums):
#             ans.append(i)
        
        def addEle(a, l, r):
            if l == r:
                #ans.append(a)
                #ans.extend(list(list(a)))
                temp = []
                temp.extend(a)
                ans.append(temp)
                #print(a)
            else:
                for i in range(l, r):
                    a[l], a[i] = a[i], a[l]
                    #print(a, l, r)
                    addEle(a, l+1, r)
                    a[l], a[i] = a[i], a[l]
        
        addEle(nums, 0, len(nums))
        
        return ans