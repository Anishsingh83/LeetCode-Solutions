class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
       
        dist = [[-1] * n for _ in range(n)]
        q = deque()
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    q.append((r, c))
        
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
        
       
        heap = [(-dist[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]
        
        while heap:
            safe, r, c = heapq.heappop(heap)
            safe = -safe
            
            if r == n - 1 and c == n - 1:
                return safe
            
            if visited[r][c]:
                continue
            visited[r][c] = True
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    heapq.heappush(heap, (-min(safe, dist[nr][nc]), nr, nc))
        
        return 0