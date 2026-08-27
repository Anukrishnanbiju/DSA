class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [False] * n
        dp[0] = True
        count = 0

        for i in range(minJump, n):
            if dp[i - minJump]:
                count += 1

            if i - maxJump - 1 >= 0 and dp[i - maxJump - 1]:
                count -= 1

            if s[i] == '0' and count > 0:
                dp[i] = True

        return dp[-1]