# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return head
        
        # print(head)
        h = head
        
        
        
        while h.next is not None:
            a = h.val
            b = h.next.val
            g = math.gcd(a,b)
            # print(a,b,g)
            # ListNode n = new ListNode(g)
            temp = h.next
            h.next = ListNode(g)
            h.next.next = temp
            # print(h)
            
            h = h.next.next
        
        
        return head