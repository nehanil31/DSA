# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        p1=head
        p2=head
        for i in range(n):
            p2=p2.next
        if p2 is None:
            return head.next    
        while p2.next is not None:
            p1=p1.next
            p2=p2.next
        curr=p1.next
        p1.next=p1.next.next
        curr=None
        return head        
