class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        for i in range(len(nums2)):
            nums2[i] *= k
        
        count = 0
        nums2.sort()
        
        for i in nums1:
            if i < nums2[0]:
                continue
            for j in nums2:
                if i%j == 0:
                    count += 1
        
        return count