class Solution:
    def minLength(self, s):
        stack = []
        for ch in s:
            if stack and ((stack[-1] == 'A' and ch == 'B') or (stack[-1] == 'C' and ch == 'D')):
                stack.pop()  # Remove the matching pair
            else:
                stack.append(ch)
        return len(stack)


        