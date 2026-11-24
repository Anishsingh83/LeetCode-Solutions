class Solution:
    def maxLength(self, nums: List[int]) -> int:
        best = 2
        left = 0
        prod = 1
        for right, x in enumerate(nums):
            while gcd(prod, x) > 1:
                prod //= nums[left]
                left += 1
            prod *= x
            if right - left + 1 > best:
                best = right - left + 1
        return best             