class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        m = n // 2

        counts = [0] * 26
        for ch in s:
            counts[ord(ch) - ord('a')] += 1

        odd_count = 0
        mid_char = ""
        half_counts = [0] * 26

        for i in range(26):
            if counts[i] % 2 != 0:
                odd_count += 1
                mid_char = chr(ord('a') + i)
            half_counts[i] = counts[i] // 2

        if odd_count > 1:
            return ""

        def build_min_palindrome(first_half: str, rem_counts: list) -> str:
            left_suffix = []
            for c_idx in range(26):
                if rem_counts[c_idx] > 0:
                    left_suffix.append(chr(ord('a') + c_idx) * rem_counts[c_idx])
            left_str = first_half + "".join(left_suffix)
            if n % 2 == 1:
                return left_str + mid_char + left_str[::-1]
            return left_str + left_str[::-1]

        
        target_prefix_valid = True
        prefix_counts = [0] * 26
        for i in range(m):
            idx = ord(target[i]) - ord('a')
            prefix_counts[idx] += 1
            if prefix_counts[idx] > half_counts[idx]:
                target_prefix_valid = False
                break

        
        if target_prefix_valid:
            rem = [half_counts[i] - prefix_counts[i] for i in range(26)]
            cand = build_min_palindrome(target[:m], rem)
            if cand > target:
                return cand

        
        curr_counts = [0] * 26
        for i in range(m):
            idx = ord(target[i]) - ord('a')
            curr_counts[idx] += 1

        
        over_limit = sum(1 for i in range(26) if curr_counts[i] > half_counts[i])

        
        for k in range(m - 1, -1, -1):
            t_idx = ord(target[k]) - ord('a')

            
            was_over = curr_counts[t_idx] > half_counts[t_idx]
            curr_counts[t_idx] -= 1
            now_over = curr_counts[t_idx] > half_counts[t_idx]
            if was_over and not now_over:
                over_limit -= 1

            if over_limit == 0:
                
                for c_idx in range(t_idx + 1, 26):
                    if curr_counts[c_idx] < half_counts[c_idx]:
                        rem = [half_counts[i] - curr_counts[i] for i in range(26)]
                        rem[c_idx] -= 1
                        prefix = target[:k] + chr(ord('a') + c_idx)
                        cand = build_min_palindrome(prefix, rem)
                        if cand > target:
                            return cand

        return ""