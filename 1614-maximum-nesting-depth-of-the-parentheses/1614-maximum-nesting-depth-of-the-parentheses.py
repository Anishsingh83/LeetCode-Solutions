class Solution:
    def maxDepth(self, s: str) -> int:
        max_d = 0
        current_d = 0

        for char in s:
            if char == '(':
                current_d += 1
                max_d = max(max_d, current_d)
            elif char == ')':
                current_d -= 1
        return max_d            