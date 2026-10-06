class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open = 0
        closed = 0

        for char in s:
            if char == '(':
                open += 1
            else:
                if open > 0:
                    open -= 1
                else:
                    closed += 1
        return open + closed