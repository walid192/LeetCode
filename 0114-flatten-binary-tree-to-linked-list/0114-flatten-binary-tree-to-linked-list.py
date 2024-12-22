# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = [None]  
        
        def traversePreorder(root):
            if root:
                if prev[0]:
                    prev[0].right = root
                prev[0] = root
                
                left = root.left
                right = root.right
                
                root.left = None
                
                traversePreorder(left)
                traversePreorder(right)
        
        traversePreorder(root)