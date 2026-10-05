class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        sc = 0
        d = 0
        for i in range(len(s)):
            if s[i] == '(':
                d += 1
            else:
                d -= 1
                if s[i - 1] == '(':
                    sc += 1 << d
        return sc      