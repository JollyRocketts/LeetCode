class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        idx = 0
        count = 0
        n = len(pieces)
        new = []
        
        while True:
            count += 1
            flag = False
            
            for i in range(len(pieces)):
                if pieces[i][0] == arr[idx]:
                    # print("FBF")
                    # print(count)
                    new.extend(pieces[i])
                    idx += len(pieces[i])
                    flag = True
                    break
            
            # print(idx)
            
            if flag == False or count == n+1:
                break
                
            pieces.pop(i)
                
                
        # if idx == len(arr):
        #     return True
        # else:
        #     return False
        
        if arr == new:
            return True
        else:
            return False