class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        count = 0
        idx = 0
        
        for i in range(len(mat)):
            temp = Counter(mat[i])[1]
            if temp>count:
                idx = i
                count = temp
                
        return [idx, count]