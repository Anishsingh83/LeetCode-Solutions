class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        @lru_cache(None)
        def dp(i, m):
            return 0 if i == n else max(
                suffix[i] - dp(i + x, max(m, x))
                for x in range(1, min(2 * m, n - i) + 1)
            )

        return dp(0, 1)