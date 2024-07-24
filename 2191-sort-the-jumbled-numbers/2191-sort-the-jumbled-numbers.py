class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        new = []
        ans = []
        
        for i in nums:
            temp = ""
            for j in str(i):
                temp += str(mapping[int(j)])
            new.append(int(temp))
            
        for i in sorted(zip(nums, new), key = lambda x:x[1]):
            ans.append(i[0])
            
        return ans