class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        first = True
        middle = True
        if word[0].islower():
            first = False
        if word[1].islower():
            middle = False
        if first == False and middle == True:
            return False
        for i in range(2,len(word)):
            if word[i].isupper() and  middle == False:
                return False
            elif word[i].islower() and first == True and middle == True:
                return False
        return True