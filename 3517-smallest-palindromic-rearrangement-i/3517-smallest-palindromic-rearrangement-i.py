class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = Counter(s)
        left = []
        mid = ""

        for c in sorted(freq):
            left.append(c * (freq[c] // 2))
            if freq[c] % 2:
                mid = c

        left = "".join(left)
        return left + mid + left[::-1]