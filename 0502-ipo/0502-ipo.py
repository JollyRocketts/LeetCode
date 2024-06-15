class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        group = sorted(zip(capital, profits))
        idx = -1
        hp = []
        for i in range(k):
            #idx = -1
            #idx -= 1
            while idx < len(group) - 1 and group[idx + 1][0] <= w:
                '''if group[idx + 1][1] > m:
                    m = group[idx + 1][1]
                    s = idx + 1'''
                heapq.heappush(hp, -group[idx + 1][1])
                idx += 1
            if not hp:
                break
            #p = max(group[:idx+1], key = lambda x:x[1])
            #w += p[1]
            #group.remove(p)
            w -= heapq.heappop(hp)
        return w
    
    