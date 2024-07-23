from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        ans = []
        # ans.extend([sorted(Counter(nums).items(), key = lambda x: x[1])[0][0]]*3)
        # print([sorted(Counter(nums).items(), key = lambda x: x[1])[0][0]]*3)
        for i in sorted(Counter(nums).items(), key = lambda x: (x[1], -x[0])):
            # print(i)
            ans.extend([i[0]]*Counter(nums)[i[0]])
            
        return ans