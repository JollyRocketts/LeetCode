class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        incr = True
        prev = -1
        
        for i in arr:
            if (i>prev and incr == True) or (i<prev and incr == False):
                prev = i
            elif i != prev and incr == True:
                incr = False
                prev = i
            else:
                return False
            
        if incr == False and arr[0]<arr[1]:
            return True
        else:
            return False