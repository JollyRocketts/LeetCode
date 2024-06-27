class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        l = edges[0][0]
        r = edges[0][1]
        for i in range(1,len(edges)):
            if l in edges[i] and r not in edges[i]:
                return l
            elif r in edges[i] and l not in edges[i]:
                return r