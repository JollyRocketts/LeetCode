class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if bits[-1] == 1:
            return False
        else:
            l = len(bits)
            if l == 1 or bits[-2] == 0:
                return True
            else:
                i = 0
                flag = True
                while i<l:
                    if bits[i] == 1:
                        i += 2
                        flag = False
                    else:
                        i += 1
                        flag = True
                return flag