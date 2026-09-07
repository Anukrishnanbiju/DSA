class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        dp = [0] * 26

        for c in s:
            i = ord(c) - 97
            dp[i] = (sum(dp) + 1) % MOD

        return sum(dp) % MOD