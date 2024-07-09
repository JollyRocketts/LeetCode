class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if n*m != len(original):
            return []
        
        curr = 0
        ans = []
        
        for i in range(m):
            ans.append(original[curr:curr+n])
            curr = curr+n
            
        return ans