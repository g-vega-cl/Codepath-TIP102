import unittest
from typing import List
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Create heap
        self.heap = nums
        heapq.heapify(self.heap)

        # Limit heap to size k
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # Upon add(val), add new val to heap
        heapq.heappush(self.heap, val)

        # Remove k + 1 largest val from heap
        heapq.heappop(self.heap)

        # Return kth largest val in heap
        return self.heap[0]

class KthLargestTest(unittest.TestCase):
    def test_kth_largest_happy_case(self):
        kthLargest = KthLargest(3, [4, 5, 8, 2])
        self.assertEqual(kthLargest.add(3),4)
        self.assertEqual(kthLargest.add(5), 5)
        self.assertEqual(kthLargest.add(10), 5)
        self.assertEqual(kthLargest.add(9), 8)
        self.assertEqual(kthLargest.add(4), 8)

    def test_kth_largest_edge_case(self):
        kthLargest = KthLargest(1, [4, 5, 8, 2])
        self.assertEqual(kthLargest.add(10),10)
        self.assertEqual(kthLargest.add(15), 15)
        self.assertEqual(kthLargest.add(10), 15)
        self.assertEqual(kthLargest.add(10), 15)
        self.assertEqual(kthLargest.add(10), 15)

    def test_kth_largest_multiple_spaces(self):
        kthLargest = KthLargest(3, [4, 5, 8, 2])
        self.assertEqual(kthLargest.add(10),5)
        self.assertEqual(kthLargest.add(15), 8)
        self.assertEqual(kthLargest.add(10), 10)
        self.assertEqual(kthLargest.add(30), 10)
        self.assertEqual(kthLargest.add(4), 10)


if __name__ == '__main__':
    unittest.main()