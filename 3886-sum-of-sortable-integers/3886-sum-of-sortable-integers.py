from typing import List

class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        target = sorted(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True

            for i in range(0, n, k):
                block = nums[i:i + k]
                expected = target[i:i + k]

                if sorted(block) != expected:
                    valid = False
                    break

                if k > 1:
                    descents = sum(
                        block[j] > block[(j + 1) % k]
                        for j in range(k)
                    )

                    if descents > 1:
                        valid = False
                        break

            if valid:
                ans += k

        return ans