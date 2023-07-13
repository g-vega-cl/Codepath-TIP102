import unittest
from typing import List

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        def helper(i, distance):
            if i < 0 or i > len(s) - 1 or res[i] <= distance:
                return
            res[i] = distance
            helper(i + 1, distance + 1)
            helper(i - 1, distance + 1)
        
        res = [len(s) for _ in range(len(s))]
        for i, char in enumerate(s):
            if char == c:
                helper(i, 0)
        
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_shortestToChar(self):
        # Happy cases
        self.assertEqual(self.sol.shortestToChar("loveleetcode", "e"), [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0])
        self.assertEqual(self.sol.shortestToChar("aaab", "b"), [3, 2, 1, 0])

        # Edge case
        self.assertEqual(self.sol.shortestToChar("b", "b"), [0])


if __name__ == "__main__":
    unittest.main()
