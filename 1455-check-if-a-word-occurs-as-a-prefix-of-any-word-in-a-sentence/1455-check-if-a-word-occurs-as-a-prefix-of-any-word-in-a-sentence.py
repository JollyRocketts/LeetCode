class Solution:
    def isPrefixOfWord(self, s: str, w: str) -> int:
        s = s.split(" ")
        
        for i in range(len(s)):
            if s[i][:len(w)] == w:
                return i+1
            
        return -1