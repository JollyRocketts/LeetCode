class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ans = []
        
        for i in sorted(zip(names, heights), key = lambda x: -x[1]):
            ans.append(i[0])
            
        return ans