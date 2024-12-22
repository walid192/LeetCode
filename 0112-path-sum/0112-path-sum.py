# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def isLeaf(node):
            return not node.left and not node.right
        
        
        def dfs(root,target):
            if not root:
                return False
		
            stack=[(root,root.val)]
            
            while stack:
                current,s=stack.pop()
		
                if (s==target and isLeaf(current)):
                    return True

                if current.right:
                    stack.append((current.right,s+current.right.val))

                if current.left:
                    stack.append((current.left,s+current.left.val))
            return False
        
        return dfs(root,targetSum)

        