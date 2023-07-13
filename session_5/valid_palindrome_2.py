import unittest


class Solution(object):
    def validPalindrome(self, s):
        def isPalindrome(left, right, count):
            if count > 1:
                return False
            while left < right:
                if s[left] != s[right]:
                    return isPalindrome(left+1, right, count+1) or isPalindrome(left, right-1, count+1)
                left += 1
                right -= 1
            return True

        return isPalindrome(0, len(s)-1, 0)


# Test the code with the provided test cases
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_validPalindrome(self):
        # Happy cases
        self.assertTrue(self.sol.validPalindrome("aba"))
        self.assertFalse(self.sol.validPalindrome("abc"))

        # Edge case
        self.assertTrue(self.sol.validPalindrome("abca"))

if __name__ == "__main__":
    unittest.main()