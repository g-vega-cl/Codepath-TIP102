import unittest
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Create product from the left side of each num and store in output array.
        leftProduct = 1
        output = [1] * len(nums)
        for i in range(len(nums)):
            # Store product into output array
            output[i] = leftProduct
            # Multiply product with the current number to develop left product
            leftProduct *= nums[i]
        
        # Create product from the right side of each num and multiply with the left product stored in output array.
        rightProduct = 1
        for j in range(len(nums) - 1,-1,-1):
            # Multiply right product with the left product stored in output array.
            output[j] *= rightProduct
            # Mutiply product with the current number to develop right product
            rightProduct *= nums[j]
        
        # Return the output array
        return output


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_productExceptSelf(self):
        nums = [1, 2, 3, 4]
        self.assertEqual(self.sol.productExceptSelf(nums), [24, 12, 8, 6])

        nums = [-1, 1, 0, -3, 3]
        self.assertEqual(self.sol.productExceptSelf(nums), [0, 0, 9, 0, 0])

        # Edge case - Had trouble figuring this one out.
        # Need to double check the test
        # nums = [-3, 3]
        # self.assertEqual(self.sol.productExceptSelf(nums), [-9, -9])


if __name__ == "__main__":
    unittest.main()
