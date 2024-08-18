class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)
        
        for i in range(1, n+1):
            ans[i] = Counter(format(i, 'b'))['1']
            # ans[i] = Counter(f'{bin(i):08b}')['1']
            
            # '{:08b}'.format(bin(i)))
        return ans