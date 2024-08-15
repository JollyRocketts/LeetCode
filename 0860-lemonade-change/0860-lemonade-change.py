class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        if bills[0] != 5:
            return False
        
        sto = [0]*4
        
        for i in bills:
            sto[i//5 - 1] += 1
            
            if i == 10:
                if sto[0] < 1:
                    return False
                else:
                    sto[0] -= 1
            
            if i == 20:
                if sto[1] < 1:
                    if sto[0] < 3:
                        return False
                    else:
                        sto[0] -= 3
                elif sto[0] < 1:
                    return False
                else:
                    sto[0] -= 1
                    sto[1] -= 1
                    
        return True