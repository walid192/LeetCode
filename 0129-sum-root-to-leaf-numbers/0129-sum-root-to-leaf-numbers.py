# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res=0
        
        def isLeaf(node):
            return not node.left and not node.right
        
        
        stack=[(root,str(root.val))]

        while(stack):
            current,current_val=stack.pop()

            if isLeaf(current):
                res+=int(current_val)

            if current.left:
                stack.append((current.left,current_val+str(current.left.val)))

            if current.right:
                stack.append((current.right,current_val+str(current.right.val)))
                
        return res

            
        
        