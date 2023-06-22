# You are a product manager and currently leading a team to develop a new product. 
# Unfortunately, the latest version of your product fails the quality check. 
# Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, 
# which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether version is bad. 
# Implement a function to find the first bad version. You should minimize the number of calls to the API.

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def isBadVersion(version: int) -> bool:
    # Specify the custom index where bad versions start
    return version >= custom_index

class Solution:

    def firstBadVersion(self, n: int) -> int:
        # Initialize left and right pointers
        l, r = 1, n
        # While left pointer is less than right pointer we have not exhausted the versions
        while l < r:
            # Get the mid point of the two pointers
            mid = (l + r) // 2

            # Check if mid point is bad or not
            if isBadVersion(mid):
                # If mid point is bad then there might be more bad versions before it, shift right pointer and check for earlier bad version.
                r = mid
            else:
                # If mid point is good then we know that everything to the left is good, shift left pointer to check for bad version in right half
                l = mid + 1
        # Return the right pointer for first bad version
        return r
    
solution = Solution()

# Test case 1: Custom index is at the first version
custom_index = 1
result = solution.firstBadVersion(5)
expected_result = custom_index
print(f"Custom index: {custom_index}, Result: {result}, Expected: {expected_result}")
assert result == expected_result

# Test case 2: Custom index is at the last version
custom_index = 10
result = solution.firstBadVersion(10)
expected_result = custom_index
print(f"Custom index: {custom_index}, Result: {result}, Expected: {expected_result}")
assert result == expected_result

# Test case 3: Custom index is in the middle
custom_index = 5
result = solution.firstBadVersion(8)
expected_result = custom_index
print(f"Custom index: {custom_index}, Result: {result}, Expected: {expected_result}")
assert result == expected_result

# Test case 4: Only one version (Edge case)
custom_index = 1
result = solution.firstBadVersion(1)
expected_result = custom_index
print(f"Custom index: {custom_index}, Result: {result}, Expected: {expected_result}")
assert result == expected_result