class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        tot = 0
        ans = []
        
        for i in nums:
            if i%2 == 0:
                tot += i
                
        for val, ind in queries:
            flag = True
            if nums[ind]%2 == 1:
                flag = False
            nums[ind] += val
            
            #was odd, now even
            if flag == False and nums[ind]%2==0:
                tot += nums[ind]
               
            #was even, still even
            if flag == True and nums[ind]%2 == 0:
                tot += val
                
            #was even, now odd
            if flag == True and nums[ind]%2 != 0:
                tot -= (nums[ind]-val)
                
            ans.append(tot)
            # print(nums)
            
        return ans