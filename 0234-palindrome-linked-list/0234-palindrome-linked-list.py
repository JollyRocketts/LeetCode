# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = []
        
        while head is not None:
            temp.append(head.val)
            head = head.next
            
        if len(temp) == 1:
            return True
        
        # print(temp[:len(temp)//2])
        # print(temp[-1:-len(temp)//2-1:-1])
        if temp[:len(temp)//2] == temp[-1:-(len(temp)//2)-1:-1]:
            return True
        else:
            return False