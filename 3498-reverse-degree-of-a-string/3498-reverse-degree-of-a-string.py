class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0

        for i, ch in enumerate(s):
            reversed_pos = 26 - (ord(ch) - ord('a'))
            string_pos = i + 1

            ans += reversed_pos * string_pos

        return ans