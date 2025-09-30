# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        prev=None
        
        while temp:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front
        return prev 
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        if head is None or head.next is None:
            return True
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        newhead=self.reverse(slow.next)
        first=head
        second=newhead
        while second is not None:
            if first.val!=second.val:
                return False
                self.reverse(newhead)
            first=first.next
            second=second.next
        self.reverse(newhead)
        return True    


        
