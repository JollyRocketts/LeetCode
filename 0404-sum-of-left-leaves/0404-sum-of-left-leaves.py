# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def ls(root,flag):
            if not root:
                return 0
            if flag and not root.left and not root.right:
                return root.val
            else:
                return ls(root.left,1)+ls(root.right,0)
        return ls(root,0)
