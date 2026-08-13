class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        tree = [None] * (4 * n)
        arr = list(s)

        def merge(left, right):
            if left is None:
                return right
            if right is None:
                return left

            l_char, l_right, l_pre, l_suf, l_best, l_len = left
            r_left, r_char, r_pre, r_suf, r_best, r_len = right

            length = l_len + r_len
            prefix = l_pre
            suffix = r_suf
            best = l_best if l_best > r_best else r_best

            if l_right == r_left:
                mid_run = l_suf + r_pre
                if mid_run > best:
                    best = mid_run
                if l_pre == l_len:
                    prefix = l_len + r_pre
                if r_suf == r_len:
                    suffix = l_suf + r_len

            return (l_char, r_char, prefix, suffix, best, length)

        def build(node, start, end):
            if start == end:
                c = arr[start]
                tree[node] = (c, c, 1, 1, 1, 1)
                return
            mid = (start + end) // 2
            build(node * 2, start, mid)
            build(node * 2 + 1, mid + 1, end)
            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def update(node, start, end, index, char):
            if start == end:
                tree[node] = (char, char, 1, 1, 1, 1)
                return
            mid = (start + end) // 2
            if index <= mid:
                update(node * 2, start, mid, index, char)
            else:
                update(node * 2 + 1, mid + 1, end, index, char)
            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        build(1, 0, n - 1)

        ans = []
        for char, index in zip(queryCharacters, queryIndices):
            if arr[index] != char:
                arr[index] = char
                update(1, 0, n - 1, index, char)
            ans.append(tree[1][4])

        return ans