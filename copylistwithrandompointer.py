"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp=head
        while temp is not None:
            newnode=Node(temp.val)
            newnode.next=temp.next
            temp.next=newnode
            temp=temp.next.next
        temp=head
        while temp is not None:
            newnode=temp.next
            if  temp.random is not None:

                newnode.random=temp.random.next
            else:
                newnode.random=None    
            temp=temp.next.next
        dummy=Node(-1)
        res=dummy
        temp=head
        while temp is not None:
            res.next=temp.next
            temp.next=temp.next.next
            res=res.next
            temp=temp.next
        return dummy.next        
        
