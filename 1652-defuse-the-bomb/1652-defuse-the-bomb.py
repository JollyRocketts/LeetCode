class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        temp = [0 for j in range(len(code))]
        for i in range(len(code)):
            if k>0:
                temp[i] = sum([code[x] if x<len(code) else code[x-len(code)] for x in range(i+1,i+1+k)])
            elif k<0:
                temp[i] = sum([code[x] for x in range(i-1,i-1+k,-1)])
            else:
                temp[i] = 0
        return temp