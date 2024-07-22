class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # return mainTank*10 + min(mainTank//5, additionalTank)*10
        
        dist = 0
        spent = 0
        
        while mainTank != 0:
            # mainTank -= 1
            
            spent += 1
            dist += 10
            
            if spent == 5 and additionalTank != 0:
                spent = 0
                additionalTank -= 1
                continue
            
            mainTank -= 1
                
        return dist