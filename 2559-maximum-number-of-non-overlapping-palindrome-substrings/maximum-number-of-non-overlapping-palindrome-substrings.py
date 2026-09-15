class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        dp = [bytearray(n) for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
                    dp[i][j] = 1

        ans = 0
        end = -1

        for r in range(n):
            for l in range(end + 1, r - k + 2):
                if dp[l][r]:
                    ans += 1
                    end = r
                    break

        return ans