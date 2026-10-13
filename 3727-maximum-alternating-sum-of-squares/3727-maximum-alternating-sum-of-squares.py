class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squared = sorted([x * x for x in nums], reverse=True)
        n = len(squared)
        half = (n + 1) // 2
        return sum(squared[:half]) - sum(squared[half:])