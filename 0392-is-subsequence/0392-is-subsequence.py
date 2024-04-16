class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = 'abcdefghijklmnopqrstuvwxyz'
        for i in s:
            l = l.replace(i,'')
        for j in l:
            t = t.replace(j,'')
        p = len(s)
        q = len(t)
        k = 0
        m = 0
        while True:
            if k == p:
                return True
            if k+m == q:
                return False
            if s[k] == t[k+m]:
                k += 1
            else:
                m += 1