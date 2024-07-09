class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        last = 0
        
        for i in s.split(" "):
            if i.isdigit():
                if int(i)>last:
                    last = int(i)
                else:
                    return False
                
        return True