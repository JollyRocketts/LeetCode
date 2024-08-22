class Solution:
    def bitwiseComplement(self, n: int) -> int:
        b = format(n, 'b')
        return 2**len(b) + ~n