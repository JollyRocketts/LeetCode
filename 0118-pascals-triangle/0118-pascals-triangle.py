class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l = []
        l.append([1])
        if numRows == 1:
            return l
        else:
            l.append([1,1])
            if numRows == 2:
                return l
            
        for i in range(1,numRows-1):
            temp = [1]
            #print(l[i])
            for j in range(len(l[i])-1):
                temp.append(l[i][j]+l[i][j+1])
            temp.append(1)
            l.append(temp)
            #print(l)
            
        return l