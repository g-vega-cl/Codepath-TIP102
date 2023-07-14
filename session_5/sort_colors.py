from typing import List
import unittest

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l, mid, r = 0, 0, len(nums) - 1
        while mid <= r:
            if nums[mid] == 0:
                nums[l], nums[mid] = nums[mid], nums[l]
                l += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[r] = nums[r], nums[mid]
                r -= 1

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sortColors(self):
        # Happy cases
        nums = [2, 0, 2, 1, 1, 0]
        self.sol.sortColors(nums)
        self.assertEqual(nums, [0, 0, 1, 1, 2, 2])

        nums = [2, 0, 1]
        self.sol.sortColors(nums)
        self.assertEqual(nums, [0, 1, 2])

        # Edge case
        nums = [2, 2, 2, 2, 2, 2]
        self.sol.sortColors(nums)
        self.assertEqual(nums, [2, 2, 2, 2, 2, 2])

if __name__ == "__main__":
    unittest.main()
