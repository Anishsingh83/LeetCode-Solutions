class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        pref = list(accumulate(stones))
        ans = pref[-1]
        for p in reversed(pref[1:-1]):
            ans = max(ans, p - ans)
        return ans        