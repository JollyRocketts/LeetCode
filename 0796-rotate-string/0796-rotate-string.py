class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        for _ in range(len(s)):
            if s == goal:
                return True
            temp = s[1:]
            temp2 = s[0]
            s = temp + temp2
            
        return False