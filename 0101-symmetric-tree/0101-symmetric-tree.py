# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def invertTree(root):
            if root:
                left=root.left
                root.left=invertTree(root.right)
                root.right=invertTree(left)
                
            return root
        
        
        def isSame(p,q):
            if not p and not q:
                return True
            
            if not p or not q:
                return False
            
            if not p.val==q.val:
                return False
            
            return isSame(p.left,q.left) and isSame(p.right,q.right)
        
        right=invertTree(root.right)
        return isSame(root.left,root.right)
            
        