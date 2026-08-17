from functools import cache

class Solution:
    def stoneGameV(self, a):
        n = len(a)
        s = [0] * (n + 1)

        for i in range(n):
            s[i + 1] = s[i] + a[i]

        @cache
        def dp(l, r):
            if l >= r:
                return 0

            ans = left = 0
            right = s[r + 1] - s[l]

            for k in range(l, r):
                left += a[k]
                right -= a[k]

                if left < right:
                    if ans >= 2 * left:
                        continue
                    ans = max(ans, left + dp(l, k))

                elif left > right:
                    if ans >= 2 * right:
                        break
                    ans = max(ans, right + dp(k + 1, r))

                else:
                    ans = max(ans,
                              left + dp(l, k),
                              right + dp(k + 1, r))

            return ans

        return dp(0, n - 1)