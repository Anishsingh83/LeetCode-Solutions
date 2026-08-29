class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        sorted_nums = sorted((val, idx) for idx, val in enumerate(nums))
        
        n = len(nums)
        ans = [0] * n
        
        i = 0
        while i < n:
            j = i
            while j + 1 < n and sorted_nums[j + 1][0] - sorted_nums[j][0] <= limit:
                j += 1
            
            indices = sorted(sorted_nums[k][1] for k in range(i, j + 1))
            
            for k in range(i, j + 1):
                ans[indices[k - i]] = sorted_nums[k][0]
                
            i = j + 1
            
        return ans