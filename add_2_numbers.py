# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy=ListNode(0)
        temp=dummy
        h1=l1
        h2=l2
       
        c=0
        while (h1 is not None or h2 is not None) or c:
            summ=0
            if h1 is not None:
                summ=summ+h1.val
                h1=h1.next
            if h2 is not None:
                summ=summ+h2.val
                h2=h2.next
            summ=summ+c
            c=summ//10
            node=ListNode(summ%10)
            temp.next=node
            temp=temp.next
        return dummy.next    




         



        
