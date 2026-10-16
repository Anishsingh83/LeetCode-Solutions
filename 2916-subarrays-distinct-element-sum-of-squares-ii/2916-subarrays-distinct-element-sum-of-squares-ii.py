class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        
        tree_sum = [0] * (4 * n)
        tree_sq = [0] * (4 * n)
        lazy = [0] * (4 * n)
        
        def push(node, l, r):
            if lazy[node] != 0:
                v = lazy[node]
                mid = (l + r) // 2
                
                
                left = 2 * node
                tree_sq[left] = (tree_sq[left] + 2 * v * tree_sum[left] + v * v * (mid - l + 1)) % MOD
                tree_sum[left] = (tree_sum[left] + v * (mid - l + 1)) % MOD
                lazy[left] = (lazy[left] + v) % MOD
                
                
                right = 2 * node + 1
                tree_sq[right] = (tree_sq[right] + 2 * v * tree_sum[right] + v * v * (r - mid)) % MOD
                tree_sum[right] = (tree_sum[right] + v * (r - mid)) % MOD
                lazy[right] = (lazy[right] + v) % MOD
                
                lazy[node] = 0

        def update(node, l, r, ql, qr, v):
            if ql <= l and r <= qr:
                tree_sq[node] = (tree_sq[node] + 2 * v * tree_sum[node] + v * v * (r - l + 1)) % MOD
                tree_sum[node] = (tree_sum[node] + v * (r - l + 1)) % MOD
                lazy[node] = (lazy[node] + v) % MOD
                return
            push(node, l, r)
            mid = (l + r) // 2
            if ql <= mid:
                update(2 * node, l, mid, ql, qr, v)
            if qr > mid:
                update(2 * node + 1, mid + 1, r, ql, qr, v)
            tree_sum[node] = (tree_sum[2 * node] + tree_sum[2 * node + 1]) % MOD
            tree_sq[node] = (tree_sq[2 * node] + tree_sq[2 * node + 1]) % MOD

        last = {}
        ans = 0
        
        for j in range(n):
            x = nums[j]
            prev_idx = last.get(x, -1)
            
            update(1, 0, n - 1, prev_idx + 1, j, 1)
            last[x] = j
            ans = (ans + tree_sq[1]) % MOD
            
        return ans