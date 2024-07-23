class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        n = 0
        curr = 1
        res = [0]*num_people
        
        while curr<=candies:
            res[n] += curr
            candies -= curr
            curr += 1
            n += 1
            if n == num_people:
                n = 0
        
        res[n] += candies
        
        return res