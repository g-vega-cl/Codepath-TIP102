class Solution:
    def isValid(self, s):
        if s == "":
            return True

        # Create a Stack which will store the brackets.
        stack = [s[0]]

        # Process each bracket of the expression one at a time.
        for i in range(1,len(s)):
            # If encounter a closing bracket, then check the element on top of the stack. 
            if s[i] == ')':
                # If the element at the top of the stack is an opening bracket of the same type, then pop it off the stack and continue processing. Else, this implies an invalid expression. 
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif s[i] == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            elif s[i] == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            else:
                # If encounter an opening bracket, push it onto the stack.
                stack.append(s[i])

        # In the end, if we are left with a stack still having elements, then this implies an invalid expression.
        return not stack
    
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

isValid = Solution().test(Solution().isValid)
print(isValid == None)
