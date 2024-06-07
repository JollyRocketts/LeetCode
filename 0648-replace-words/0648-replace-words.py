class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        d = sorted(dictionary, key = len)
        words = sentence.split(" ")
        sen = ""
        for i in words:
            flag = False
            for j in d:
                if i[:len(j)] == j:
                    flag = True
                    sen += j
                    sen += " "
                    break
            if flag == False:
                sen += i
                sen += " "
        return sen[:len(sen)-1]