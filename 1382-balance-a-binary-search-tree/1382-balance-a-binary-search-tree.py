# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        def inorder(root, arr):
            if root is None:
                return 0
            inorder(root.left, arr)
            arr.append(root.val)
            inorder(root.right, arr)
            
        arr = []
        inorder(root, arr)
        
        l = 0
        r = len(arr) - 1
        
        def builder(l, r, arr):
            if l>r:
                return None
            mid = (l + r)//2
            root2 = TreeNode(arr[mid])
            root2.left = builder(l, mid-1, arr)
            root2.right = builder(mid+1, r, arr)
            return root2
        
        root2 = TreeNode(None)
        return builder(l, r, arr)