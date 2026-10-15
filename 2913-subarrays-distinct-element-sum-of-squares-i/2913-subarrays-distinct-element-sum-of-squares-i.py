class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ts = 0
        n = len(nums)

        for i in range(n):
            de = set()
            for j in range(i, n):
                de.add(nums[j])
                c = len(de)
                ts += c * c
        return ts