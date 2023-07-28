from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
  
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Check if the tree is empty. If it is, return a new TreeNode with node value of val
        if not root:
            return TreeNode(val)
        
        # Recursively traverse the tree in pre-order fashion
        if root.val > val:
            # If node.val > input value: traverse the left subtree
            root.left = self.insertIntoBST(root.left, val)
        else:
            # Else traverse the right subtree
            root.right = self.insertIntoBST(root.right, val)
        
        # Return the root of the tree
        return root