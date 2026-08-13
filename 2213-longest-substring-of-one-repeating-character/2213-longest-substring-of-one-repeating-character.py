from sortedcontainers import SortedList

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        arr = list(s)
        bounds = SortedList([0] + [i for i in range(1, n) if arr[i] != arr[i-1]])
        lens = SortedList()
        for idx, st in enumerate(bounds):
            en = bounds[idx+1] if idx+1 < len(bounds) else n
            lens.add(en - st)

        def get_run(i):
            pos = bounds.bisect_right(i) - 1
            st = bounds[pos]
            en = bounds[pos+1] if pos+1 < len(bounds) else n
            return st, en

        ans = []
        for c, i in zip(queryCharacters, queryIndices):
            if arr[i] == c:
                ans.append(lens[-1])
                continue

            st, en = get_run(i)
            lens.remove(en - st)
            bounds.remove(st)

            if i > st:
                bounds.add(st)
                lens.add(i - st)
            if i + 1 < en:
                bounds.add(i + 1)
                lens.add(en - i - 1)
            bounds.add(i)
            lens.add(1)
            arr[i] = c

            if i + 1 < n and arr[i + 1] == c:
                st1, en1 = get_run(i)
                st2, en2 = get_run(i + 1)
                lens.remove(en1 - st1)
                lens.remove(en2 - st2)
                bounds.remove(st2)
                lens.add(en2 - st1)

            if i > 0 and arr[i - 1] == c:
                st1, en1 = get_run(i - 1)
                st2, en2 = get_run(i)
                lens.remove(en1 - st1)
                lens.remove(en2 - st2)
                bounds.remove(st2)
                lens.add(en2 - st1)

            ans.append(lens[-1])

        return ans