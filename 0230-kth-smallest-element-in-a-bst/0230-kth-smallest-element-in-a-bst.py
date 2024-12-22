# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        res=[]
        def inorderTraverse(root):
            if root:
                inorderTraverse(root.left)
                res.append(root.val)
                inorderTraverse(root.right)
            return res
        res=inorderTraverse(root)
        return res[k-1]
                
        