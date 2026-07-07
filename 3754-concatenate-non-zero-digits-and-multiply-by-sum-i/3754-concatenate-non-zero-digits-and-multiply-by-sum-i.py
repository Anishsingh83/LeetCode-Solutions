class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = ''.join(ch for ch in str(n) if ch != '0')
        x = int(s) if s else 0
        return x * sum(int(ch) for ch in str(x))        