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
        
        dummy=Node(2)
        current=dummy
        
        dummyHead=head
        while (dummyHead):
            value=dummyHead.val
            current.next=Node(value)
            
            dummyHead=dummyHead.next
            current=current.next
         
        
        current=dummy.next
        dummyHead=head
        
        while(dummyHead):
            n=dummyHead.random
            
            fast=head
            suiv=dummy.next
            
            while (fast!=n):
                fast=fast.next
                suiv=suiv.next
            current.random=suiv
            
            current=current.next
            dummyHead=dummyHead.next
        
        return dummy.next
            
        
        