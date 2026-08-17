class Solution:
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)

        prefix = [0]

        for v in stoneValue:
            prefix.append(prefix[-1] + v)

        mid = list(range(n))
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = stoneValue[i]

        max_score = 0

        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1

                while prefix[mid[i]] - prefix[i] < prefix[j + 1] - prefix[mid[i]]:
                    mid[i] += 1

                p = mid[i]
                max_score = 0

                if prefix[p] - prefix[i] == prefix[j + 1] - prefix[p]:
                    max_score = max(dp[i][p - 1], dp[j][p])
                else:
                    if i <= p - 2:
                        max_score = max(max_score, dp[i][p - 2])

                    if p <= j:
                        max_score = max(max_score, dp[j][p])

                dp[i][j] = max(
                    dp[i][j - 1],
                    prefix[j + 1] - prefix[i] + max_score
                )

                dp[j][i] = max(
                    dp[j][i + 1],
                    prefix[j + 1] - prefix[i] + max_score
                )

        return max_score