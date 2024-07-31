class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort()
        
        for i in range(-1,-len(arr)-1,-1):
            if arr.count(arr[i]) == arr[i]:
                return arr[i]
            
        return -1