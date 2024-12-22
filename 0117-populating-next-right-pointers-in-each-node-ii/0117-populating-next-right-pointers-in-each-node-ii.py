"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return None 

        result = []
        queue = deque([root])
        
        while queue:
            level = []
            prev=None
            for _ in range(len(queue)):
                current = queue.popleft()
                level.append(current)
                
                if prev:
                    prev.next=current
                prev=current

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            result.append(level)

        return root