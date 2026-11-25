class Solution:
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        base1, mod1 = 1315423911, (1 << 61) - 1
        base2, mod2 = 2654435761, 10**9 + 7

        p1 = [1] * (n + 1)
        p2 = [1] * (n + 1)
        h1 = [0] * (n + 1)
        h2 = [0] * (n + 1)

        for i, val in enumerate(nums):
            x = val + 1
            p1[i + 1] = (p1[i] * base1) % mod1
            p2[i + 1] = (p2[i] * base2) % mod2
            h1[i + 1] = (h1[i] * base1 + x) % mod1
            h2[i + 1] = (h2[i] * base2 + x) % mod2

        def has_unique(length: int) -> bool:
            counts = Counter()
            for start in range(n - length + 1):
                end = start + length
                g1 = (h1[end] - h1[start] * p1[length]) % mod1
                g2 = (h2[end] - h2[start] * p2[length]) % mod2
                counts[(g1, g2)] += 1
            return any(freq == 1 for freq in counts.values())

        low, high = 1, n
        ans = n
        while low <= high:
            mid = (low + high) // 2
            if has_unique(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans