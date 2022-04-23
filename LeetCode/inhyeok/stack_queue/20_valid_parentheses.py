class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        for ss in s:
            if ss not in table:
                stack.append(ss)
            elif not stack or table[ss] != stack.pop():
                return False
        return len(stack) == 0