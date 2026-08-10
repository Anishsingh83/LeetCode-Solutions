class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @lru_cache(None)
        def dp(x):
            if x == 0:
                return False

            for i in range(1, isqrt(x) + 1):
                if not dp(x - i * i):
                    return True

            return False

        return dp(n)       