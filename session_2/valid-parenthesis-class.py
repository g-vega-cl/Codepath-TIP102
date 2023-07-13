# code-here
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets. Open brackets must be closed in the correct order. Every close bracket has a corresponding open bracket of the same type.

# 1. Create a stack. We will store the brackets here
# 2. Process brackets - Add open brackets to the stack
# 3. Keep doing that until we meet a closing bracket.
# 4. If we meet a closing bracket, check the last open bracket in the stack, and check if it matches.
from collections import deque
class Solution:
    def isValid(self,string):
        stack = []
        for s in string:
            if s in "({[":
                stack.append(s)
            else:
                if (s == ")" & stack[-1] == "(") :
                    stack.pop()
                elif (s == "}" & stack[-1] == "{"):
                    stack.pop()
                elif (s == "]" & stack[-1] == "["):
                    stack.pop()
                else:
                    return False

    def test(self, isValid):
        assert isValid("()") == True
        assert isValid("()[]{}") == True
        assert isValid("(]") == False
        assert isValid("([)]") == False
        assert isValid("{[]}") == True
        assert isValid("]") == False
        assert isValid("((") == False
        assert isValid("){") == False
        assert isValid(" ") == True
        assert isValid("()") == True
        assert isValid("()[]{}") == True
        assert isValid("{[)") == False
        assert isValid("{([)") == False
        assert isValid("{ [ { } ] }") == True
        assert isValid(" ") == True

isValid = Solution().test(Solution().isValid)
print(isValid == None)