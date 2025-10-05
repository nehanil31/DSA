# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
        #sorting using merge sort
    def mergeTwoSortedLinkedLists(self,list1, list2):
        dummyNode = ListNode(-1)
        temp = dummyNode
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next 
        if list1 is not None:
            temp.next = list1
        else:
            temp.next = list2
        return dummyNode.next                
    def findMiddle(self,head):
    # If the list is empty or has only one node
    # the middle is the head itself
        if head is None or head.next is None:
            return head

    # Initializing slow and fast pointers
        slow = head
        fast = head.next

    # Move the fast pointer twice as
    # fast as the slow pointer

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
    # When the fast pointer reaches the end,
    # the slow pointer will be at the middle

        return slow
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        middle =self.findMiddle(head)

    # Divide the list into two halves
        right = middle.next
        middle.next = None
        left = head

    # Recursively sort the left and right halves
        left = self.sortList(left)
        right = self.sortList(right)
        return self.mergeTwoSortedLinkedLists(left, right)    

        
