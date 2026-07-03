class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        adj = [[] for _ in range(n)]
        costs = set([0])
        for u, v, c in edges:
            adj[u].append((v, c))
            costs.add(c)
        costs = sorted(costs)

        def feasible(mn):
            INF = float('inf')
            dist = [INF] * n
            dist[0] = 0
            indeg = [0] * n
            valid_edges = [[] for _ in range(n)]
            for u in range(n):
                if u != 0 and u != n - 1 and not online[u]:
                    continue
                for v, c in adj[u]:
                    if v != 0 and v != n - 1 and not online[v]:
                        continue
                    if c < mn:
                        continue
                    valid_edges[u].append((v, c))
                    indeg[v] += 1

            from collections import deque
            order = []
            q = deque([i for i in range(n) if indeg[i] == 0])
            temp_indeg = indeg[:]
            while q:
                u = q.popleft()
                order.append(u)
                for v, c in valid_edges[u]:
                    temp_indeg[v] -= 1
                    if temp_indeg[v] == 0:
                        q.append(v)

            for u in order:
                if dist[u] == INF:
                    continue
                for v, c in valid_edges[u]:
                    if dist[u] + c <= k and dist[u] + c < dist[v]:
                        dist[v] = dist[u] + c
            return dist[n - 1] != INF

        lo, hi = 0, len(costs) - 1
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if feasible(costs[mid]):
                ans = costs[mid]
                lo = mid + 1
            else:
                hi = mid - 1
        return ans