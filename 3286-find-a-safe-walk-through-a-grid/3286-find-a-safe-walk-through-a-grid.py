class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        visited = [[0] * n for _ in range(m)]
        q = deque()
        
        start_health = health - grid[0][0]
        if start_health <= 0:
            return False
        
        visited[0][0] = start_health
        q.append((0, 0, start_health))
        
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        
        while q:
            r, c, hp = q.popleft()
            
            if r == m - 1 and c == n - 1:
                return True
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    new_hp = hp - grid[nr][nc]
                    if new_hp > 0 and new_hp > visited[nr][nc]:
                        visited[nr][nc] = new_hp
                        q.append((nr, nc, new_hp))
        
        return False        