class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m = len(coins)
        n = len(coins[0])
        NEG = -10**15

        dp = [[NEG] * 3 for _ in range(n)]

        for i in range(m):
            cur = [[NEG] * 3 for _ in range(n)]

            for j in range(n):
                x = coins[i][j]

                if i == 0 and j == 0:
                    cur[j][0] = x
                    if x < 0:
                        cur[j][1] = 0
                    continue

                for k in range(3):
                    # Come from above
                    if i > 0:
                        cur[j][k] = max(
                            cur[j][k],
                            dp[j][k] + x
                        )

                    # Come from left
                    if j > 0:
                        cur[j][k] = max(
                            cur[j][k],
                            cur[j - 1][k] + x
                        )

                    # Neutralize this robber
                    if x < 0 and k > 0:
                        if i > 0:
                            cur[j][k] = max(
                                cur[j][k],
                                dp[j][k - 1]
                            )

                        if j > 0:
                            cur[j][k] = max(
                                cur[j][k],
                                cur[j - 1][k - 1]
                            )

            dp = cur

        return max(dp[-1])