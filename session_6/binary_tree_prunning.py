from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # the idea is to use DFS to traverse the tree
    # if the current subtree satisfies one of the following conditions
    # 1. root value is 1
    # 2. left sub tree contains 1 
    # 3. right sub tree contains 1
    # then we return `root`
    # otherwise, we return None
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if root is None, then return None
        if root is None: return None
        # DFS on left sub tree
        root.left = self.pruneTree(root.left)
        # DFS on right sub tree
        root.right = self.pruneTree(root.right)
        # !root->left means the left sub tree doesn't contain 1
        # !root->right means the right sub tree doesn't contain 1
        # !root->val means the current node value is 0
        # for this case, return None
        # else we can keep the node
        if root.left is None and root.right is None and root.val == 0: return None
        return root
    
# sol = Solution()

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_pruneTree(self):
        # Happy cases
        root1 = TreeNode(1, None, TreeNode(0, TreeNode(0), TreeNode(1)))
        expected_output1 = TreeNode(1, None, TreeNode(0, None, TreeNode(1)))
        self.assertEqual(self.sol.pruneTree(root1).__dict__, expected_output1.__dict__)

        root2 = TreeNode(1, TreeNode(0), TreeNode(1, TreeNode(0), TreeNode(0)))
        expected_output2 = TreeNode(1, None, TreeNode(1, None, None))
        self.assertEqual(self.sol.pruneTree(root2).__dict__, expected_output2.__dict__)

        # Edge case
        root3 = TreeNode(0, TreeNode(0, TreeNode(0, TreeNode(0, TreeNode(0))), None), None)
        self.assertEqual(self.sol.pruneTree(root3), None)

if __name__ == "__main__":
    unittest.main()