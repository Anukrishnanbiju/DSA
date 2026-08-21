from math import gcd

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            ans = 0
            n = len(coins)

            for mask in range(1, 1 << n):
                v = 1
                bits = 0

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        v = lcm(v, coins[i])

                        if v > x:
                            break

                else:
                    if bits % 2:
                        ans += x // v
                    else:
                        ans -= x // v

            return ans

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left        