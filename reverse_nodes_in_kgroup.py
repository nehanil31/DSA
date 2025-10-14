# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLinkedList(self,head):
        temp=head
        prev=None
        while temp is not None:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front
        return prev
    def getkthnode(self,temp,k):
        k=k-1
        while temp is not None and k>0:
            k=k-1
            temp=temp.next
        return temp


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp=head
        prevlast=None
        while temp is not None:
            kthnode=self.getkthnode(temp,k)
            if kthnode is None:
                if prevlast:
                    prevlast.next = temp
                break
            nextnode=kthnode.next
            kthnode.next=None
            self.reverseLinkedList(temp)
            if temp==head:
                head=kthnode
            else:
                prevlast.next=kthnode
            prevlast=temp
            temp=nextnode
        return head                

        
