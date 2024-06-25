# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        arr = []
    
        def inorder(root, arr):
            if root is None:
                return 0
            inorder(root.left, arr)
            arr.append(root.val)
            inorder(root.right, arr)
    
        inorder(root, arr)
        
        def inorderC(root,arr):
            if root is None:
                return 0
            inorderC(root.left, arr)
            if root.val == arr[0]:
                root.val = sum(arr)
                arr.pop(0)
            inorderC(root.right, arr)
        
        inorderC(root, arr)
        
        return root