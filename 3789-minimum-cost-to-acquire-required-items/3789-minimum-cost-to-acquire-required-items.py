
class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        common = min(need1, need2)
        remaining = max(need1, need2) - common

        return common * min(costBoth, cost1 + cost2) + remaining * min(costBoth, cost1 if need1 > need2 else cost2)
