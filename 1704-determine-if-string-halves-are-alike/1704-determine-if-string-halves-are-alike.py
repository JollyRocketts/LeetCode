from collections import Counter

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        h1 = Counter(s[:len(s)//2])
        h2 = Counter(s[len(s)//2:])
        
        vowels = ["a","e","i","o","u","A","E","I","O","U"]
        
        tot1 = sum(list(h1[i] for i in vowels))
        tot2 = sum(list(h2[i] for i in vowels))
        
        return tot1==tot2