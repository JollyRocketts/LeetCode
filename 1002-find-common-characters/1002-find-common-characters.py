import collections
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        arr = collections.Counter(words[0])
        for i in range(1,len(words)):
            arr &= collections.Counter(words[i])
        return list(arr.elements())