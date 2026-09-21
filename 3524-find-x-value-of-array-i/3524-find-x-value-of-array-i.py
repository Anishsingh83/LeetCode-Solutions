class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        rlt = [0] * k
        dp = [0] * k
        
        for num in nums:
            mod = num % k
            n_dp = [0] * k
            
            for r in range(k):
                if dp[r] > 0:
                    n_dp[(r * mod) % k] += dp[r]
                    
            n_dp[mod] += 1
            
            for r in range(k):
                rlt[r] += n_dp[r]
                
            dp = n_dp
            
        return rlt