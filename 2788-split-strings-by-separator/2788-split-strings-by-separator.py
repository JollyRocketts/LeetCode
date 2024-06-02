class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        new = []
        for i in words:
            new.append(i.split(separator))
        new2 = [xs for x in new for xs in x if xs != ""]
        return new2