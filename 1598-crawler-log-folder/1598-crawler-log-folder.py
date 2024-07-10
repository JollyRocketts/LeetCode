class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        
        for i in logs:
            if i[-2] == ".":
                if len(i) != 2 and i[-3] == "." and count != 0:
                    count -= 1
                else:
                    continue
            else:
                count += 1
        
        return count