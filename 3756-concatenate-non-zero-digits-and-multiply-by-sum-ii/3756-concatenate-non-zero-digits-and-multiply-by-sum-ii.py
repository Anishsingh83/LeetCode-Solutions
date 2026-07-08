class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7

        pos = []
        digits = []

        for i, ch in enumerate(s):
            if ch != '0':
                pos.append(i)
                digits.append(int(ch))

        n = len(digits)

        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        prefNum = [0] * (n + 1)
        prefSum = [0] * (n + 1)

        for i in range(n):
            prefNum[i + 1] = (prefNum[i] * 10 + digits[i]) % MOD
            prefSum[i + 1] = prefSum[i] + digits[i]

        ans = []

        for l, r in queries:
            left = bisect_left(pos, l)
            right = bisect_right(pos, r) - 1

            if left > right:
                ans.append(0)
                continue

            length = right - left + 1

            num = (
                prefNum[right + 1]
                - prefNum[left] * pow10[length]
            ) % MOD

            digit_sum = prefSum[right + 1] - prefSum[left]

            ans.append((num * digit_sum) % MOD)

        return ans