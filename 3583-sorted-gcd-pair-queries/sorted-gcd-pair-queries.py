from collections import Counter
from itertools import accumulate
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)
        cnt = Counter(nums)
        gcd = [0] * (mx + 1)

        for i in range(mx, 0, -1):
            total = 0

            for j in range(i, mx + 1, i):
                total += cnt[j]
                gcd[i] -= gcd[j]

            gcd[i] += total * (total - 1) // 2

        prefix = list(accumulate(gcd))

        return [bisect_right(prefix, q) for q in queries]