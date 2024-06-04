# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def post(root):
            if root.val == 1:
                return True
            elif root.val == 0:
                return False
            else:
                a = post(root.left)
                b = post(root.right)
                if root.val == 2: 
                    return a | b
                else:
                    return a & b
        res = post(root)
        return res