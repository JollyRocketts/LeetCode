class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = -1
        while digits[i] == 9:
            if abs(i) == len(digits):
                digits[i] = 0
                digits.insert(0, 1)
                return digits
            digits[i] = 0
            i -= 1
        digits[i] += 1
        return digits