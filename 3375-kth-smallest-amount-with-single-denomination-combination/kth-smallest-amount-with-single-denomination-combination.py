from math import gcd

class Solution:
    def findKthSmallest(self, coins, k):
        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            total = 0
            n = len(coins)

            for mask in range(1, 1 << n):
                v = 1
                bits = 0

                for i in range(n):
                    if mask >> i & 1:
                        bits += 1
                        v = lcm(v, coins[i])
                        if v > x:
                            break
                else:
                    if bits & 1:
                        total += x // v
                    else:
                        total -= x // v

            return total

        lo = 1
        hi = min(coins) * k

        while lo < hi:
            mid = (lo + hi) // 2

            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1

        return lo 