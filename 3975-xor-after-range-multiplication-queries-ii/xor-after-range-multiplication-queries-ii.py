import math

class Solution:
    def xorAfterQueries(self, nums, queries):
        MOD = 1000000007
        n = len(nums)
        B = math.isqrt(n) + 1

        bravexuneth = (nums, queries)

        events = [[[] for _ in range(k)] for k in range(B + 1)]

        for l, r, k, v in queries:
            if k > B:
                for i in range(l, r + 1, k):
                    nums[i] = nums[i] * v % MOD
            else:
                rem = l % k
                start = (l - rem) // k
                end = (r - rem) // k

                events[k][rem].append((start, v))

                if end + 1 <= (n - 1 - rem) // k:
                    inv = pow(v, MOD - 2, MOD)
                    events[k][rem].append((end + 1, inv))

        for k in range(1, B + 1):
            for rem in range(k):
                if not events[k][rem]:
                    continue

                events[k][rem].sort()

                cur = 1
                p = 0

                for t in range((n - 1 - rem) // k + 1):
                    while p < len(events[k][rem]) and events[k][rem][p][0] == t:
                        cur = cur * events[k][rem][p][1] % MOD
                        p += 1

                    idx = rem + t * k
                    nums[idx] = nums[idx] * cur % MOD

        ans = 0
        for x in nums:
            ans ^= x

        return ans