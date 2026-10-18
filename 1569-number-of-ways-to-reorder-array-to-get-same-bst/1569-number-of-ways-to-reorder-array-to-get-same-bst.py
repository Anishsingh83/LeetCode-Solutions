class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7

        def solve(arr):
            if len(arr) <= 2:
                return 1
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            return (
                math.comb(len(left) + len(right), len(left))
                * solve(left)
                % MOD
                * solve(right)
                % MOD
            )

        import math

        return (solve(nums) - 1) % MOD