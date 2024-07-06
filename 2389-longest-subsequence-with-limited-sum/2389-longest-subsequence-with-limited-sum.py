class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        acc = []
        tot = 0
        
        for i in nums:
            tot += i
            acc.append(tot)
        
        ans = []
        
        for i in queries:
            j = 0
            while j<len(nums) and acc[j]<=i:
                j += 1
            ans.append(j)
            
        return ans