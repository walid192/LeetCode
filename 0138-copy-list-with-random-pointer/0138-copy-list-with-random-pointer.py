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
        
        if not head:
            return None
        
        value_map={}
        next_map={}
        random_map={}
        
        current=head
        
        while(current):
            value_map[current]=current.val
            next_map[current]=current.next
            random_map[current]=current.random
            current=current.next
            
        otn_map={}
        
        for key,value in value_map.items():
            new=Node(value)
            otn_map[key]=new
            
        
        for key,value in next_map.items():
            otn_map[key].next=otn_map.get(value)
            
        for key,value in random_map.items():
            otn_map[key].random=otn_map.get(value)
            
        return otn_map[head]
        
            
        
        