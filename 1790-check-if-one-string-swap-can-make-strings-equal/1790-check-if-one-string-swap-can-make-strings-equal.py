class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        temp = []
        for n,i in enumerate(s1):
            if i!=s2[n]:
                temp.append(i)
                temp.append(s2[n])
        if len(temp) == 4 and temp == temp[::-1]:
            return True
        else:
            return False