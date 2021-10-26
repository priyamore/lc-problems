'''
Problem Statement:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Example 1:
Input: s = "([)]"
Output: false

Example 2:
Input: s = "{[]}"
Output: true
'''

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        d = {')':'(','}':'{',']':'['}
        
        for char in s:
		#if opening brackets push in stack
            if char in d.values():
                stack.append(char)
			#if closing brackets, pop from stack and compare to check if the matched parentheses was popped	
            else:
                if len(stack) > 0:
                    if stack.pop()!= d[char]:
                        return False
                
                else:
                    return False
		#After processing all chars, stack should be empty. if it is not empty means parentheses are unbalanced
        if len(stack) > 0:
            return False
        return True