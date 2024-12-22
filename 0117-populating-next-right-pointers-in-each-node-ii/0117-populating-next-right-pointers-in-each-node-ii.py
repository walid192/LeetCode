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
            return None  # Handle the edge case where the tree is empty

        result = []
        queue = [root]  # Initialize the queue with the root node
        
        while queue:
            level = []
            for _ in range(len(queue)):  # Iterate through the current level
                current = queue.pop(0)  # Dequeue the first element
                level.append(current)

                # Add left and right children to the queue if they exist
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            result.append(level)

        # Set the 'next' pointers for each level
        for level in result:
            for i in range(len(level) - 1):  # Skip appending None explicitly
                level[i].next = level[i + 1]

        return root