from functools import cache

class Solution:
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        @cache
        def dp(l, r):
            if l >= r:
                return 0

            ans = 0
            left = 0
            right = prefix[r + 1] - prefix[l]

            for k in range(l, r):
                left += stoneValue[k]
                right -= stoneValue[k]

                if left < right:
                    ans = max(ans, left + dp(l, k))

                elif left > right:
                    ans = max(ans, right + dp(k + 1, r))

                else:
                    ans = max(
                        ans,
                        left + dp(l, k),
                        right + dp(k + 1, r)
                    )

            return ans

        return dp(0, n - 1)