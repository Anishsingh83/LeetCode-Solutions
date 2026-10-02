class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def backtrack(open_n, close_n, path):
            if open_n == close_n == n:
                res.append("".join(path))
                return
            if open_n < n:
                path.append("(")
                backtrack(open_n + 1, close_n, path)
                path.pop()
            if close_n < open_n:
                path.append(")")
                backtrack(open_n, close_n + 1, path)
                path.pop()

        backtrack(0, 0, [])
        return res