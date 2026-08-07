class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        def factorize(t):
            f = {2:0,3:0,5:0,7:0}
            for p in (2,3,5,7):
                while t % p == 0:
                    f[p] += 1
                    t //= p
            return f, t

        f0, rem0 = factorize(t)
        if rem0 != 1:
            return "-1"

        digit_factors = {
            1:(0,0,0,0), 2:(1,0,0,0), 3:(0,1,0,0), 4:(2,0,0,0),
            5:(0,0,1,0), 6:(1,1,0,0), 7:(0,0,0,1), 8:(3,0,0,0), 9:(0,2,0,0),
        }

        need2, need3, need5, need7 = f0[2], f0[3], f0[5], f0[7]

        n = len(num)
        digits = [int(c) for c in num]

        
        INF = float('inf')
        dp = [[INF]*(need3+1) for _ in range(need2+1)]
        dp[0][0] = 0
        options = [(3,0),(2,0),(1,0),(0,2),(0,1),(1,1)]
        for i in range(need2+1):
            for j in range(need3+1):
                if dp[i][j] == INF:
                    continue
                for (di,dj) in options:
                    ni = min(need2, i+di)
                    nj = min(need3, j+dj)
                    if dp[i][j]+1 < dp[ni][nj]:
                        dp[ni][nj] = dp[i][j]+1
        min_digits_table = dp  

        def min_digits_needed(n2, n3):
            n2 = min(n2, need2)
            n3 = min(n3, need3)
            if n2 <= 0 and n3 <= 0:
                return 0
            return min_digits_table[n2][n3]

        def feasible(n2, n3, n5, n7, L):
            if n7 > L: return False
            L2 = L - n7
            if n5 > L2: return False
            L3 = L2 - n5
            return min_digits_needed(n2, n3) <= L3

        def build_suffix(n2, n3, n5, n7, L):
            if not feasible(n2, n3, n5, n7, L):
                return None
            out = []
            r2, r3, r5, r7 = n2, n3, n5, n7
            remaining_len = L
            for pos in range(L):
                remaining_len -= 1
                placed = False
                for d in range(1, 10):
                    a2,a3,a5,a7 = digit_factors[d]
                    nn2 = max(0, r2-a2); nn3 = max(0, r3-a3)
                    nn5 = max(0, r5-a5); nn7 = max(0, r7-a7)
                    if feasible(nn2, nn3, nn5, nn7, remaining_len):
                        out.append(d)
                        r2,r3,r5,r7 = nn2,nn3,nn5,nn7
                        placed = True
                        break
                if not placed:
                    return None
            return out

        
        prefix2 = [0]*(n+1)
        prefix3 = [0]*(n+1)
        prefix5 = [0]*(n+1)
        prefix7 = [0]*(n+1)
        for idx, d in enumerate(digits):
            a2,a3,a5,a7 = digit_factors.get(d, (0,0,0,0)) 
            prefix2[idx+1] = prefix2[idx] + a2
            prefix3[idx+1] = prefix3[idx] + a3
            prefix5[idx+1] = prefix5[idx] + a5
            prefix7[idx+1] = prefix7[idx] + a7

        has_zero_prefix = [False]*(n+1)  
        for idx in range(n):
            has_zero_prefix[idx+1] = has_zero_prefix[idx] or (digits[idx] == 0)

        
        if not has_zero_prefix[n]:
            if (prefix2[n] >= need2 and prefix3[n] >= need3 and
                prefix5[n] >= need5 and prefix7[n] >= need7):
                return num

        best = None
        for i in range(n-1, -1, -1):
            if has_zero_prefix[i]:   
                continue
            pa2, pa3, pa5, pa7 = prefix2[i], prefix3[i], prefix5[i], prefix7[i]
            orig_d = digits[i]
            found_here = False
            for d in range(orig_d+1, 10):
                x2,x3,x5,x7 = digit_factors[d]
                r2 = max(0, need2-(pa2+x2))
                r3 = max(0, need3-(pa3+x3))
                r5 = max(0, need5-(pa5+x5))
                r7 = max(0, need7-(pa7+x7))
                L = n - i - 1
                suf = build_suffix(r2, r3, r5, r7, L)
                if suf is not None:
                    best = digits[:i] + [d] + suf
                    found_here = True
                    break
            if found_here:
                break

        if best is not None:
            return ''.join(map(str, best))

        
        L = n + 1
        while True:
            for d in range(1, 10):
                x2,x3,x5,x7 = digit_factors[d]
                r2 = max(0, need2-x2)
                r3 = max(0, need3-x3)
                r5 = max(0, need5-x5)
                r7 = max(0, need7-x7)
                suf = build_suffix(r2, r3, r5, r7, L-1)
                if suf is not None:
                    return ''.join(map(str, [d]+suf))
            L += 1
            if L > n + 60:
                return "-1"