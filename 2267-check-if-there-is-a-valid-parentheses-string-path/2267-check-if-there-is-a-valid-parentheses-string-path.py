class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        if (m + n - 1) % 2 != 0:
            return False
            
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        visited = set()

        def dfs(i: int, j: int, balance: int) -> bool:
            balance += 1 if grid[i][j] == '(' else -1
            
            if balance < 0 or balance > (m + n - 1) // 2:
                return False
                
            if i == m - 1 and j == n - 1:
                return balance == 0

            state = (i, j, balance)
            if state in visited:
                return False
            visited.add(state)

            if i + 1 < m and dfs(i + 1, j, balance):
                return True
            if j + 1 < n and dfs(i, j + 1, balance):
                return True

            return False

        return dfs(0, 0, 0)