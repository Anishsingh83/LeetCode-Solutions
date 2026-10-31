class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        right = [[0] * n for _ in range(m)]
        down = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    ways = 1
                else:
                    ways = (right[i][j] + down[i][j]) % MOD

                if grid[i][j] == 1:
                    if right[i][j] and i + 1 < m:
                        down[i + 1][j] = (down[i + 1][j] + right[i][j]) % MOD

                    if down[i][j] and j + 1 < n:
                        right[i][j + 1] = (right[i][j + 1] + down[i][j]) % MOD
                else:
                    if j + 1 < n:
                        right[i][j + 1] = (right[i][j + 1] + ways) % MOD

                    if i + 1 < m:
                        down[i + 1][j] = (down[i + 1][j] + ways) % MOD

        return (right[m - 1][n - 1] + down[m - 1][n - 1]) % MOD