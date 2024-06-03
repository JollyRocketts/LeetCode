class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i<len(arr)-1:
            if arr[i] == 0:
                temp = arr[i+1:len(arr)-1]
                arr[i+1] = arr[i]
                for j in range(i+2, len(arr)):
                    arr[j] = temp[j-i-2]
                i += 2
            else:
                i += 1