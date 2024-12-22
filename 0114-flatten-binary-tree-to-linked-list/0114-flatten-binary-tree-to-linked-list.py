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
        result=[]
        
        def traversePreorder(root):
            if root:
                result.append(root)
                traversePreorder(root.left)
                traversePreorder(root.right)
            return result
        
        res=traversePreorder(root)
        
        for i, node in enumerate(res[:-1]):
            node.left=None
            node.right=res[i+1]
