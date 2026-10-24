class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def to_days(date_str):
            m, d = map(int, date_str.split('-'))
            return sum(days[:m - 1]) + d
            
        a1 = to_days(arriveAlice)
        l1 = to_days(leaveAlice)
        a2 = to_days(arriveBob)
        l2 = to_days(leaveBob)
        
        start = max(a1, a2)
        end = min(l1, l2)
        
        return max(0, end - start + 1)