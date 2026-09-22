class SegmentTree:
    def __init__(self, nums: List[int], k: int):
        self.n = len(nums)
        self.k = k
        self.total_prod = [1] * (4 * self.n)
        
        self.counts = [[0] * k for _ in range(4 * self.n)]
        self._build(nums, 1, 0, self.n - 1)

    def _merge(self, tree_idx: int, left_idx: int, right_idx: int):
        l_prod = self.total_prod[left_idx]
        r_prod = self.total_prod[right_idx]
        
        self.total_prod[tree_idx] = (l_prod * r_prod) % self.k
        
        
        for rem in range(self.k):
            self.counts[tree_idx][rem] = self.counts[left_idx][rem]
            

        for rem in range(self.k):
            cnt = self.counts[right_idx][rem]
            if cnt > 0:
                new_rem = (l_prod * rem) % self.k
                self.counts[tree_idx][new_rem] += cnt

    def _build(self, nums: List[int], tree_idx: int, l: int, r: int):
        if l == r:
            val_rem = nums[l] % self.k
            self.total_prod[tree_idx] = val_rem
            self.counts[tree_idx][val_rem] = 1
            return
        
        mid = (l + r) // 2
        self._build(nums, 2 * tree_idx, l, mid)
        self._build(nums, 2 * tree_idx + 1, mid + 1, r)
        self._merge(tree_idx, 2 * tree_idx, 2 * tree_idx + 1)

    def update(self, tree_idx: int, l: int, r: int, idx: int, val: int):
        if l == r:
            val_rem = val % self.k
            self.total_prod[tree_idx] = val_rem
            
            for rem in range(self.k):
                self.counts[tree_idx][rem] = 0
            self.counts[tree_idx][val_rem] = 1
            return
        
        mid = (l + r) // 2
        if idx <= mid:
            self.update(2 * tree_idx, l, mid, idx, val)
        else:
            self.update(2 * tree_idx + 1, mid + 1, r, idx, val)
        self._merge(tree_idx, 2 * tree_idx, 2 * tree_idx + 1)

    def query(self, tree_idx: int, l: int, r: int, ql: int, qr: int):
        
        if ql <= l and r <= qr:
            return self.total_prod[tree_idx], self.counts[tree_idx]
        
        mid = (l + r) // 2
        if qr <= mid:
            return self.query(2 * tree_idx, l, mid, ql, qr)
        if ql > mid:
            return self.query(2 * tree_idx + 1, mid + 1, r, ql, qr)
        
        l_prod, l_counts = self.query(2 * tree_idx, l, mid, ql, qr)
        r_prod, r_counts = self.query(2 * tree_idx + 1, mid + 1, r, ql, qr)
        
        res_prod = (l_prod * r_prod) % self.k
        res_counts = list(l_counts)
        
        for rem in range(self.k):
            cnt = r_counts[rem]
            if cnt > 0:
                new_rem = (l_prod * rem) % self.k
                res_counts[new_rem] += cnt
                
        return res_prod, res_counts


class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        st = SegmentTree(nums, k)
        ans = []
        
        for idx, val, start, x in queries:
            st.update(1, 0, n - 1, idx, val)
            _, counts = st.query(1, 0, n - 1, start, n - 1)
            ans.append(counts[x])
            
        return ans