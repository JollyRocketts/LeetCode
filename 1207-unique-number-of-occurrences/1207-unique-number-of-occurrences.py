from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        # print(sorted(list(Counter(arr).values())))
        # print(list(set(Counter(arr).values())))
        
        if sorted(list(Counter(arr).values())) == sorted(list(set(Counter(arr).values()))):
            return True
        else:
            return False