class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        k = k1 + k2
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]

        if sum(diff) <= k:
            return 0

        freq = [0] * (max(diff) + 1)

        for d in diff:
            freq[d] += 1

        for i in range(len(freq) - 1, 0, -1):
            count = min(k, freq[i])
            freq[i] -= count
            freq[i - 1] += count
            k -= count

            if k == 0:
                break

        return sum(i * i * freq[i] for i in range(len(freq)))