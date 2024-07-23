class Solution:
    def thousandSeparator(self, n: int) -> str:
        
        if len(str(n)) <= 3:
            return str(n)
        
        s = list(str(n))
        l = len(s)-3
        
        while l>0:
            s.insert(l, ".")
            l -= 3
            
        return "".join(i for i in s)