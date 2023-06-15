
from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linked_list(lst):
    dummy = ListNode(0)
    ptr = dummy
    for i in lst:
        ptr.next = ListNode(i)
        ptr = ptr.next
    return dummy.next

def linked_list_to_list(head):
    res = []
    while head is not None:
        res.append(head.val)
        head = head.next
    return res

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy head. This will be our reference to our return list + Create a curr pointer that helps us build the return list
        dummyNode = curr = ListNode()
        
        # Initialize a variable to store the remainder value, if any, as we compute the sum. 
        remainder = 0
        
        # Traverse the two lists while our two pointers is not null and remainder is not 0.
        while l1 or l2 or remainder:
            
            # Find the values at each pointer
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            
            # Find and store their sum
            total = num1 + num2 + remainder
            singleDigitTotal = total % 10
            
            # Calculate the carry over value, if any
            remainder = total // 10 
            
            # Create and attach a new node with summed value to the return list
            curr.next = ListNode(singleDigitTotal)
            
            # Repeat with next nodes
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        # Return dummy.next
        return dummyNode.next
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_addTwoNumbers(self):
        l1 = list_to_linked_list([2, 4, 3])
        l2 = list_to_linked_list([5, 6, 4])
        result = self.sol.addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_list(result), [7, 0, 8])

        l1 = list_to_linked_list([0])
        l2 = list_to_linked_list([0])
        result = self.sol.addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_list(result), [0])

        l1 = list_to_linked_list([9, 9, 9, 9, 9, 9, 9])
        l2 = list_to_linked_list([9, 9, 9, 9])
        result = self.sol.addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_list(result), [8, 9, 9, 9, 0, 0, 0, 1])

if __name__ == '__main__':
    unittest.main()