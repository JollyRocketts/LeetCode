class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        group = sorted(zip(capital, profits))
        idx = 0
        hp = []
        for i in range(k):
            while idx < len(group) and group[idx][0] <= w:
                heapq.heappush(hp, -group[idx][1])
                idx += 1
            if not hp:
                break
            w -= heapq.heappop(hp)
        return w
    
    