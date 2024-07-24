class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        
        for i in nums1:
            temp = nums2.index(i)+1
            
            while temp < len(nums2):
                
                if nums2[temp] > i:
                    ans.append(nums2[temp])
                    break
                    
                temp += 1
            
            if temp == len(nums2):
                ans.append(-1)
                
        
        return ans
            