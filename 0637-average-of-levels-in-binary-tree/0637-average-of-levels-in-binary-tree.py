# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        
        queue=deque([root])
        res=[]
        
        while queue:
            l=len(queue)
            s=0
            
            for i in range(l):
                current=queue.popleft()
                
                s+=current.val
                
                if i==l-1:
                    res.append(s/l)
                    
                if current.left:
                    queue.append(current.left)
                    
                if current.right:
                    queue.append(current.right)
                    
        return res
                
                
            
        