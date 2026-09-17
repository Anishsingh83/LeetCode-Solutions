class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        INF = float('inf')

        dp = [INF] * (n + 1)
        
        ans = INF
        left = 0
        curr = 0
        
        for right in range(n):
            curr += arr[right]
            

            while curr > target:
                curr -= arr[left]
                left += 1
                

            dp[right + 1] = dp[right]
            
            if curr == target:
                length = right - left + 1
                
                
                if dp[left] != INF:
                    ans = min(ans, length + dp[left])
                
                
                dp[right + 1] = min(dp[right + 1], length)
                
        return -1 if ans == INF else ans