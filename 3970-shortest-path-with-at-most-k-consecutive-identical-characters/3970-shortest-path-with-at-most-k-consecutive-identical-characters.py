class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v, w))

        dist = [[[float('inf')] * (k + 1) for _ in range(26)] for _ in range(n)]

        c = ord(labels[0]) - ord('a')
        dist[0][c][1] = 0

        pq = [(0, 0, c, 1)]

        while pq:
            d, u, prev, cnt = heappop(pq)

            if d != dist[u][prev][cnt]:
                continue

            if u == n - 1:
                return d

            for v, w in graph[u]:
                curr = ord(labels[v]) - ord('a')

                if curr == prev:
                    if cnt == k:
                        continue
                    new_cnt = cnt + 1
                else:
                    new_cnt = 1

                nd = d + w

                if nd < dist[v][curr][new_cnt]:
                    dist[v][curr][new_cnt] = nd
                    heappush(pq, (nd, v, curr, new_cnt))

        return -1