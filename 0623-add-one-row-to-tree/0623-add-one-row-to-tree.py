# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            temp = root
            root = TreeNode(val)
            root.left = temp
            return root
        def dfs(root, depth):
            if depth <= 1:
                return
            if depth == 2:
                temp = root.left
                temp2 = root.right
                root.left = TreeNode(val)
                root.left.left = temp
                root.right = TreeNode(val)
                root.right.right = temp2
            if root.left:
                dfs(root.left, depth-1)
            if root.right:
                dfs(root.right, depth-1)
        dfs(root, depth)
        return root