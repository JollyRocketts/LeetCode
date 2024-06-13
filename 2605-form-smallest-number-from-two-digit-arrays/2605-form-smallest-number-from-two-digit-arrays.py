class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        if list(set(nums1)&set(nums2)) != []:
            return min(list(set(nums1)&set(nums2)))
        a = min(nums1)
        b = min(nums2)
        return min(a*10+b,b*10+a)