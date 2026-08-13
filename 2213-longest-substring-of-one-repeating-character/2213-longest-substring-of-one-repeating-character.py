class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        tree = [None] * (4 * n)
        arr = list(s)

        def merge(l, r):
            if not l: return r
            if not r: return l
            lc, lr, lp, ls, lb, ll = l
            rl, rc, rp, rs, rb, rl_ = r
            best = max(lb, rb)
            pre, suf = lp, rs
            if lr == rl:
                best = max(best, ls + rp)
                if lp == ll: pre = ll + rp
                if rs == rl_: suf = ls + rl_
            return (lc, rc, pre, suf, best, ll + rl_)

        def build(node, start, end):
            if start == end:
                tree[node] = (arr[start],) * 2 + (1, 1, 1, 1)
                return
            mid = (start + end) // 2
            build(node*2, start, mid)
            build(node*2+1, mid+1, end)
            tree[node] = merge(tree[node*2], tree[node*2+1])

        def update(node, start, end, i, c):
            if start == end:
                tree[node] = (c, c, 1, 1, 1, 1)
                return
            mid = (start + end) // 2
            update(node*2, start, mid, i, c) if i <= mid else update(node*2+1, mid+1, end, i, c)
            tree[node] = merge(tree[node*2], tree[node*2+1])

        build(1, 0, n - 1)
        ans = []
        for c, i in zip(queryCharacters, queryIndices):
            if arr[i] != c:
                arr[i] = c
                update(1, 0, n - 1, i, c)
            ans.append(tree[1][4])
        return ans