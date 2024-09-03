class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        
        if len(s) != len(goal):
            return False
        
        if s == goal:
            if Counter(s).most_common()[0][1] > 1:
                return True
            else:
                return False
        
        count = 0
        flag = False
        ans = False
        
        for i in range(len(s)):
            if s[i] != goal[i]:
                count += 1
                if flag == False:
                    temp1 = s[i]
                    temp2 = goal[i]
                    flag = True
                elif ans == False:
                    if s[i] == temp2 and goal[i] == temp1:
                        ans = True
                else:
                    return False
                        
            
        if ans == True and count == 2:
            return True
        else:
            return False