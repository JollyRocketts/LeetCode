class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        count = 0
        
        for i in range(-2, len(colors)-2):
            if colors[i]^colors[i+1] == colors[i+1]^colors[i+2] == 1:
                count += 1
                #print(i)
                
        return count