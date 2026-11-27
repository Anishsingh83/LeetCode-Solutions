class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        dp = [0] + [-10**9] * budget

        for i in range(n):
            factor, price = items[i]

            free = sum(
                1 for j in range(n)
                if i != j and items[j][0] % factor == 0
            )

            ndp = dp[:]

            for r in range(min(price, budget + 1)):
                best = -10**9

                for q in range((budget - r) // price + 1):
                    if q > 0:
                        c = r + (q - 1) * price
                        best = max(best, dp[c] - (q - 1))

                    b = r + q * price

                    if best > -10**9:
                        ndp[b] = max(ndp[b], free + q + best)

            dp = ndp

        return max(dp)