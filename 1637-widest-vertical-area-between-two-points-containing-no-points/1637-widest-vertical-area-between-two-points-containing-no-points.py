class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda x:x[0])
        maxm = 0
        
        for i in range(len(points)-1):
            if points[i][0] == points[i+1][0]:
                continue
            maxm = max(maxm, points[i+1][0] - points[i][0])
            
        return maxm