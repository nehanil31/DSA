# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        tail=head
        length=1
        count=1
        while tail.next is not None:
            length+=1
            tail=tail.next
        if k%length==0:
            return head
        k=k%length
        tail.next=head
        temp=head
        while count!=length-k:
            count+=1
            temp=temp.next
        head=temp.next
        temp.next=None
        return head



            

        
