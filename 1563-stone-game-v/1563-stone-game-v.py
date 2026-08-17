class Solution:
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)

        if n == 1:
            return 0

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]

        row_best = [[float('-inf')] * n for _ in range(n)]
        col_best = [[float('-inf')] * n for _ in range(n)]

        for i in range(n):
            row_best[i][i] = prefix[i + 1]
            col_best[i][i] = -prefix[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                total = prefix[j + 1] - prefix[i]

                lo = i
                hi = j - 1

                while lo <= hi:
                    mid = (lo + hi) // 2

                    left = prefix[mid + 1] - prefix[i]
                    right = total - left

                    if left <= right:
                        lo = mid + 1
                    else:
                        hi = mid - 1

                best = 0

                if hi >= i:
                    best = max(best, row_best[i][hi] - prefix[i])

                if lo <= j - 1:
                    best = max(best, col_best[lo + 1][j] + prefix[j + 1])

                if hi >= i and lo == hi + 1:
                    k = hi
                    left = prefix[k + 1] - prefix[i]
                    right = prefix[j + 1] - prefix[k + 1]

                    if left == right:
                        best = max(
                            best,
                            left + dp[i][k],
                            right + dp[k + 1][j]
                        )

                dp[i][j] = best

                row_best[i][j] = max(
                    row_best[i][j - 1],
                    prefix[j + 1] + dp[i][j]
                )

                col_best[i][j] = max(
                    col_best[i + 1][j],
                    dp[i][j] - prefix[i]
                )

        return dp[0][n - 1]