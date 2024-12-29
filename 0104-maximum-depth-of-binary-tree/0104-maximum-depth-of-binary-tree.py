# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        maxi=0

        queue=collections.deque([(root,1)])

        while queue:
            current,depth=queue.popleft()

            maxi=max(maxi,depth)

            if current.left:
                queue.append((current.left,depth+1))
            if current.right:
                queue.append((current.right,depth+1))

        return maxi
        
        

        