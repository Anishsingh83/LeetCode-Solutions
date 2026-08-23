class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        
        left_q = num[:half].count('?')
        right_q = num[half:].count('?')
        
        left_sum = sum(int(c) for c in num[:half] if c != '?')
        right_sum = sum(int(c) for c in num[half:] if c != '?')
        
       
        if (left_q + right_q) % 2 != 0:
            return True
            
        
        return 2 * (left_sum - right_sum) != 9 * (right_q - left_q)  