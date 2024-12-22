# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue=deque([root])
        j=0
        res=[]

        while queue:
            level=[]
            for _ in range(len(queue)):
                current=queue.popleft()

                if j%2==0:
                    level.append(current.val)
                else:
                    level=[current.val]+level

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            j+=1
            res.append(level)
        return res


        