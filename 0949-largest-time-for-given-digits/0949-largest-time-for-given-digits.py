class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        res = ""
        
        # 2  1  0
        # 3  9  9
        # 5  5  5
        # 9  9  9
        
        while 2 in arr:
            
            temp = []
            flag = False
            temp.extend(arr)
            res += "2"
            temp.remove(2)
            lim = 3
            
            while lim not in temp:
                lim -= 1
                
                if lim < 0:
                    flag = True
                    break
                    
            if flag == True:
                break
            
            res += str(lim)
            temp.remove(lim)
            
            res += ":"
            # print(arr)
            lim = 5

            while lim not in temp:
                lim -= 1

                if lim < 0:
                    flag = True
                    break
            
            if flag == True:
                break
                
            res += str(lim)
            temp.remove(lim)
            # print(temp)
            lim = 9

            while lim not in temp:
                lim -= 1
                # print(lim)
                if lim < 0:
                    flag = True
                    break
            
            if flag == True:
                break 
                
            res += str(lim)


            return res
        
        # print(":HELLO")
        
        while 1 in arr:
            
            temp = []
            flag = False
            res = ""
            temp.extend(arr)
            res += "1"
            temp.remove(1)
            
            lim = 9
            
            while lim not in temp:
                lim -= 1
                
                if lim < 0:
                    flag = True
                    break
                    
            if flag == True:
                break
                
            res += str(lim)
            # print(lim)
            temp.remove(lim)
            # print(temp)
            res += ":"
            # print(arr)
            lim = 5

            while lim not in temp:
                lim -= 1

                if lim < 0:
                    flag = True
                    break
            
            if flag == True:
                break
                
            res += str(lim)
            temp.remove(lim)
            # print(temp)
            lim = 9

            while lim not in temp:
                lim -= 1
                # print(lim)
                if lim < 0:
                    flag = True
                    break
            if flag == True:
                break
                
            res += str(lim)


            return res
            
        # print("YO")
        # print(arr)
        if 0 in arr:
            res = ""
            res += "0"
            arr.remove(0)
            
            lim = 9
            
            while lim not in arr:
                lim -= 1
                
                if lim < 0:
                    return ""
            
            res += str(lim)
            arr.remove(lim)
            
        else:
            return ""
        
        # print("HELLO")
        res += ":"
        # print(arr)
        lim = 5
            
        while lim not in arr:
            lim -= 1
            
            if lim < 0:
                    return ""
        # print("YO")    
        res += str(lim)
        arr.remove(lim)
        
        lim = 9
        # print("DAMN")    
        while lim not in arr:
            lim -= 1
            
            if lim < 0:
                    return ""
            
        res += str(lim)
        
        
        return res
        
#         curr = 2
        
#         while curr not in arr:
#             curr -= 1
            