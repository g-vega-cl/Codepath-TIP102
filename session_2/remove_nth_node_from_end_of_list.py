import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Create a dummy node and attach it to the head of the input list.
        dummy = ListNode(val=0, next = head)
        
        # Initialize 2 pointers, first and second, to point to the dummy node.
        first = dummy
        second = dummy
        
        # Advances first pointer so that the gap between first and second is n nodes apart
        for i in range(n+1):
            first = first.next
            
        # While the first pointer does not equal null move both first and second to maintain the gap and get nth node from the end
        while (first != None):
            first = first.next
            second = second.next
        
        # Delete the node being pointed to by second.
        second.next = second.next.next
        
        # Return dummy.next
        return dummy.next
    
def list_to_linked_list(lst):
    dummy = ListNode(0)
    ptr = dummy
    for i in lst:
        ptr.next = ListNode(i)
        ptr = ptr.next
    return dummy.next

def print_linked_list(head):
    while head is not None:
        print(head.val, end=" -> ")
        head = head.next
    print("None")  # signify end of list

def linked_list_to_list(head):
    lst = []
    while head is not None:
        lst.append(head.val)
        head = head.next
    return lst

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_removeNthFromEnd(self):
        head = list_to_linked_list([1,2,3,4,5])
        result = self.sol.removeNthFromEnd(head, 2)
        self.assertEqual(linked_list_to_list(result), [1,2,3,5])
        
        head = list_to_linked_list([1])
        result = self.sol.removeNthFromEnd(head, 1)
        self.assertEqual(linked_list_to_list(result), [])
        
        head = list_to_linked_list([1,2])
        result = self.sol.removeNthFromEnd(head, 2)
        self.assertEqual(linked_list_to_list(result), [2])

        head = list_to_linked_list([1,2])
        result = self.sol.removeNthFromEnd(head, 1)
        self.assertEqual(linked_list_to_list(result), [1])

# head = list_to_linked_list([1,2,3,4,5])
# answer = Solution().removeNthFromEnd(head, 2)

# print_linked_list(answer)

if __name__ == '__main__':
    unittest.main()