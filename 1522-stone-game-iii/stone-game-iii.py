from functools import cache

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        n = len(stoneValue)

        @cache
        def dp(i):
            if i >= n:
                return 0

            best = float("-inf")
            total = 0

            for j in range(i, min(i + 3, n)):
                total += stoneValue[j]
                best = max(best, total - dp(j + 1))

            return best

        ans = dp(0)

        if ans > 0:
            return "Alice"
        elif ans < 0:
            return "Bob"
        return "Tie"  