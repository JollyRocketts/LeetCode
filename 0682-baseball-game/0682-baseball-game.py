class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # l = 0
        
        tot = []
        
        for i in operations:
            if i.lstrip("-").isdigit():
                tot.append(int(i))
            elif i == "D":
                tot.append(tot[-1]*2)
            elif i == "C":
                tot.pop()
            elif i == "+":
                tot.append(tot[-1]+tot[-2])
              
        # print(tot)
        
        return sum(tot)