class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b, d in roads:
            graph[a].append((b, d))
            graph[b].append((a, d))

        visited = set()
        stack = [1]
        ans = float('inf')

        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            for neighbor, dist in graph[node]:
                ans = min(ans, dist)
                if neighbor not in visited:
                    stack.append(neighbor)

        return ans