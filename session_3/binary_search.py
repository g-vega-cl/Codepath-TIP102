# Given an array of integers nums which is sorted in ascending order, 
# and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize left and right pointers
        l, r = 0, len(nums) - 1
        
        # While left pointer is less than right pointer we have not exhausted the num list
        while l <= r:
            # Get the mid point of the two pointers 
            mid = (l + r) // 2
            
            # Check if mid point is less than, greater than, or equal to target

            # if mid point is less than target, then we know everything to the left of mid point can be eliminated from search
            if nums[mid] < target:
                l = mid + 1
            # else if mid point is greater than target, then we know everything to the right of mid point can be eliminated from search
            elif nums[mid] > target:
                r = mid - 1 
            # else the number is equal, so we return the mid index
            else:
                return mid
        
        # The left pointer is greater than the right pointers, we have exhausted the num list, return -1 
        return -1
    
def test_search():
    binary_search = Solution()

    # Test case 1: Target present in the list
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    assert binary_search.search(nums, target) == 4

    # Test case 2: Target not present in the list
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    assert binary_search.search(nums, target) == -1

    # Test case 3: Empty list
    nums = []
    target = 5
    assert binary_search.search(nums, target) == -1

    # Test case 4: Single element list (target present)
    nums = [5]
    target = 5
    assert binary_search.search(nums, target) == 0

    # Test case 5: Single element list (target not present)
    nums = [3]
    target = 5
    assert binary_search.search(nums, target) == -1

    print("All test cases pass")

# Run the test cases
test_search()