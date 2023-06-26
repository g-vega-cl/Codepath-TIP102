import unittest
from typing import List
from collections import Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Create a count of students with round sandwich and square sandwich.
        counter = Counter(students)
        
        # Start at the top of stack of sandwiches and distribute sandwich to appropriate student
        # Once no more students want the top sandwich then we cannot distribute sandwiches and we are left with students without lunch.
        for sandwich in sandwiches:
            if counter[sandwich] == 0:
                break
            counter[sandwich] -= 1
        
        # Return the total number of students without lunch. 
        return counter[0] + counter[1]
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_countStudents(self):
        students = [1,1,0,0]
        sandwiches = [0,1,0,1]
        result = self.sol.countStudents(students, sandwiches)
        self.assertEqual(result, 0)

        students = [1]
        sandwiches = [0]
        result = self.sol.countStudents(students, sandwiches)
        self.assertEqual(result, 1)

        students = [1,1,1,0,0,1]
        sandwiches = [1,0,0,0,1,1]
        result = self.sol.countStudents(students, sandwiches)
        self.assertEqual(result, 3)

if __name__ == "__main__":
    unittest.main()