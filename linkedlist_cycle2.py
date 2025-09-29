# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        vis={}
        temp=head
        
        while temp and temp.next:
            if temp not in vis:
                vis[temp]=True
            else:
                return temp
                break
            temp=temp.next    
            
        return None  
        """
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                slow=head
                while slow!=fast:
                    slow=slow.next
                    fast=fast.next
                return slow    
        return None                     
                    
        
