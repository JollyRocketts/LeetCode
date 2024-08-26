"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        ans = []
        
        def pt(root):
            if root is None:
                return
            for i in root.children:
                pt(i)
            ans.append(root.val)
            
        pt(root)
        return ans
        