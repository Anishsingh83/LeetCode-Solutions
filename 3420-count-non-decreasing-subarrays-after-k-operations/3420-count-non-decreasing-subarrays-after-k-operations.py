from typing import List
from array import array
class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        nxt = array('i', [n]) * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()

            if stack:
                nxt[i] = stack[-1]

            stack.append(i)

        levels = n.bit_length()

        up = [nxt]
        sm = [array('q', [nums[i] * (nxt[i] - i) for i in range(n)])]

        for p in range(1, levels):
            prev_up = up[-1]
            prev_sm = sm[-1]

            curr_up = array('i', [n]) * n
            curr_sm = array('q', [0]) * n

            for i in range(n):
                mid = prev_up[i]

                if mid < n:
                    curr_up[i] = prev_up[mid]
                    curr_sm[i] = prev_sm[i] + prev_sm[mid]
                else:
                    curr_sm[i] = prev_sm[i]

            up.append(curr_up)
            sm.append(curr_sm)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        def get_cost(l, r):
            cur = l
            total = 0

            for p in range(levels - 1, -1, -1):
                if up[p][cur] <= r:
                    total += sm[p][cur]
                    cur = up[p][cur]

            total += nums[cur] * (r - cur + 1)

            return total - (prefix[r + 1] - prefix[l])

        ans = 0
        l = 0

        for r in range(n):
            while l <= r and get_cost(l, r) > k:
                l += 1

            ans += r - l + 1

        return ans