class Solution:
    def greatestLetter(self, s: str) -> str:
        l = set()
        i = 0
        
        while i<len(s):
            # print(len(s))
            # print(i)
            if s[i].islower():
                l.add(s[i])
                s = s[:i] + s[i+1:]
            else:
                i += 1
        
        # print(s)
        
        flag = False
        temp = "A"
        
        for j in s:
            if j.lower() in l:
                flag = True
                temp = max(temp, j)
                
        if flag == False:
            return ""
        else:
            return temp