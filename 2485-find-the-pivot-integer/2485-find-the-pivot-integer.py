class Solution:
    def pivotInteger(self, n: int) -> int:
        # dis = 1-2*n*(n+1)
        # print(dis)
        # res = (-1 + (dis)**(1/2))/2
        # print(res)
        # if res == int(res):
        #     return res
        # else:
        #     return -1
        
        res = (n*(n+1)/2)**(1/2)
        if res == int(res):
             return int(res)
        else:
             return -1
        