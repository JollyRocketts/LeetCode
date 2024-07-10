class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        for i in range(len(s)):
            if (i+distance[ord(s[i])-97]+1<len(s) and s[i+distance[ord(s[i])-97]+1] == s[i]) or (i-distance[ord(s[i])-97]-1>=0 and s[i-distance[ord(s[i])-97]-1] == s[i]):
                continue
            else:
                return False
        
        return True