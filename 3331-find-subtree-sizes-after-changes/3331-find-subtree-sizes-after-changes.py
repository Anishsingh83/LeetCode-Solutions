class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        last = {}
        new_parent = [-1] * n

        def dfs(node):
            ch = s[node]
            old = last.get(ch)
            last[ch] = node

            for child in children[node]:
                dfs(child)

            if old is not None:
                new_parent[node] = old
            else:
                new_parent[node] = parent[node]

            if old is None:
                last.pop(ch)
            else:
                last[ch] = old

        dfs(0)

        new_children = [[] for _ in range(n)]

        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        answer = [1] * n

        def calculate(node):
            for child in new_children[node]:
                answer[node] += calculate(child)
            return answer[node]

        calculate(0)

        return answer