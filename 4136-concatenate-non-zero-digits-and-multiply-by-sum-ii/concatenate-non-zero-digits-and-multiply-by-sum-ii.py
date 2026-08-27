class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        sm = [0] * (n + 1)
        cnt = [0] * (n + 1)
        val = [0] * (n + 1)
        p10 = [1] * (n + 1)

        for i, c in enumerate(s):
            d = int(c)
            sm[i + 1] = sm[i] + d
            cnt[i + 1] = cnt[i] + (d != 0)
            val[i + 1] = val[i]
            if d:
                val[i + 1] = (val[i] * 10 + d) % MOD

        for i in range(1, n + 1):
            p10[i] = p10[i - 1] * 10 % MOD

        ans = []

        for l, r in queries:
            k = cnt[r + 1] - cnt[l]
            total = sm[r + 1] - sm[l]

            x = (val[r + 1] - val[l] * p10[k]) % MOD

            ans.append(x * total % MOD)

        return ans