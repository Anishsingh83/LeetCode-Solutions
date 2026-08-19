class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = {}

        for r, s in reservedSeats:
            rows[r] = rows.get(r, 0) | (1 << s)

        ans = (n - len(rows)) * 2

        for mask in rows.values():
            left = 0b000000111100
            middle = 0b000011110000
            right = 0b001111000000

            if mask & left == 0 and mask & right == 0:
                ans += 2
            elif mask & left == 0 or mask & middle == 0 or mask & right == 0:
                ans += 1

        return ans
