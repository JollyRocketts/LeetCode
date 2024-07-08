class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def reverse(start, end, arr):
            no_of_reverse = end-start+1
            count = 0
            #print(end)
            #print(start)
            while((no_of_reverse)//2 != count):
                arr[start+count], arr[end-count] = arr[end-count], arr[start+count]
                count += 1
            return arr

        def rotate(arr, size, d):
            start = 0
            end = size-1
            arr = reverse(start, end, arr)

            start = 0
            end = size-d-1
            arr = reverse(start, end, arr)

            start = size-d
            end = size-1
            arr = reverse(start, end, arr)
            return arr
    
        l = []
        for i in range(1,n+1):
            l.append(i)
        
        while len(l) > 1: 
            #print(l)
            nu = len(l)
            l.pop(k%nu-1)
            if nu-1 == 1:
                break
            #print(l)
            #print("\n")
            if k%nu-1 > 0:
                l = rotate(l, nu-1, k%nu-1)
                
        return l[0]