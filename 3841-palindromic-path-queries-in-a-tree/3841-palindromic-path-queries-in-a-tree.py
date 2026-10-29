class Solution:
    def palindromePath(self, n: int, edges: List[List[int]], s: str, queries: List[str]) -> List[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0
        stack = [(0, -1, 0)]

        while stack:
            u, p, state = stack.pop()
            if state == 0:
                tin[u] = timer
                timer += 1
                stack.append((u, p, 1))
                for v in reversed(adj[u]):
                    if v != p:
                        parent[v] = u
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer - 1

        LOG = n.bit_length()
        up = [parent[:]]
        up[0][0] = 0

        for k in range(1, LOG):
            prev = up[k - 1]
            up.append([prev[prev[u]] for u in range(n)])

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            k = 0
            while diff:
                if diff & 1:
                    u = up[k][u]
                diff >>= 1
                k += 1

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]

            return parent[u]

        bit = [0] * (n + 2)

        def add(i, val):
            i += 1
            while i <= n + 1:
                bit[i] ^= val
                i += i & -i

        def range_xor(l, r, val):
            add(l, val)
            if r + 1 < n:
                add(r + 1, val)

        def point_query(i):
            i += 1
            res = 0
            while i:
                res ^= bit[i]
                i -= i & -i
            return res

        chars = list(s)

        for u in range(n):
            mask = 1 << (ord(chars[u]) - ord('a'))
            range_xor(tin[u], tout[u], mask)

        ans = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                if chars[u] != c:
                    old = 1 << (ord(chars[u]) - ord('a'))
                    new = 1 << (ord(c) - ord('a'))
                    range_xor(tin[u], tout[u], old ^ new)
                    chars[u] = c
            else:
                u, v = int(parts[1]), int(parts[2])
                w = lca(u, v)

                mask = point_query(tin[u]) ^ point_query(tin[v])
                mask ^= 1 << (ord(chars[w]) - ord('a'))

                ans.append((mask & (mask - 1)) == 0)

        return ans