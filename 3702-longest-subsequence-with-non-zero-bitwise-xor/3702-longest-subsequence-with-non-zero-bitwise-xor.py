class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        x = 0
        for n in nums:
            x ^= n
        return len(nums) if x else len(nums) - 1 if max(nums) else 0 