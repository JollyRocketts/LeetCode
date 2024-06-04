class Solution:
    def oddString(self, words: List[str]) -> str:
        n = len(words[0])
        arr = []
        for i in range(len(words)):
            for j in range(1,n):
                arr.append(ord(words[i][j])-ord(words[i][j-1]))
        for i in range(len(words)): 
            if arr[i*(n-1):(i+1)*(n-1)] != arr[(i+1)*(n-1):(i+2)*(n-1)]:
                if arr[i*(n-1):(i+1)*(n-1)] != arr[(i+2)*(n-1):(i+3)*(n-1)] and arr[(i+2)*(n-1):(i+3)*(n-1)] != []:
                    return words[i]
                else:
                    return words[i+1]