class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr3 = []
        for i in arr2:
            while i in arr1:
                arr3.append(i)
                arr1.remove(i)
        if arr1 != []:
            arr1.sort()
            arr3.extend(arr1)
        return arr3