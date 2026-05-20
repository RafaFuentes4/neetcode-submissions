class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {
            "}": "{",
            ")": "(",
            "]": "[",
        }

        stack = []

        for c in s:
            if c in close_to_open:
                if not stack or close_to_open[c] != stack.pop():
                    return False
            else:
                stack.append(c)

        return True if not stack else False

