class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(n):
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s

        n = len(nums)
        indexed_nums = sorted(
            [(digit_sum(nums[i]), nums[i], i) for i in range(n)]
        )

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or indexed_nums[i][2] == i:
                continue

            cycle_size = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
                curr = indexed_nums[curr][2]
                cycle_size += 1

            if cycle_size > 1:
                swaps += cycle_size - 1

        return swaps