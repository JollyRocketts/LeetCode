class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ans = []
        s11 = s1.split()
        s22 = s2.split()
        
        unq = (set([i for i in s11]) - (set([j for j in s22]))) | (set([i for i in s22]) - (set([j for j in s11])))
        
        for i in unq:
            if s11.count(i) == 1 or s22.count(i) == 1:
                ans.append(i)
                
        return ans