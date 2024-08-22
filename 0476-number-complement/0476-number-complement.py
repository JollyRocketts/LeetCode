class Solution:
    def findComplement(self, num: int) -> int:
        bi = format(num, 'b')
        
        # print(bi)
        # c = [1]*len(str(bi))
        # co = int("".join(str(i) for i in c))
        # print(co)
        # print(bi^co)
        # return int(str(bi^co),2)
        
        return 2**(len(bi)) + ~num