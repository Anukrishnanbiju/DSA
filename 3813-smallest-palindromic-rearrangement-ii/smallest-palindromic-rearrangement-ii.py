class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        LIMIT = 1000001
        cnt = [0] * 26

        for c in s[:len(s) // 2]:
            cnt[ord(c) - 97] += 1

        m = sum(cnt)

        def count_perm(cnt, total):
            res = 1
            for c in cnt:
                if c:
                    res *= comb(total, c)
                    if res >= LIMIT:
                        return LIMIT
                    total -= c
            return res

        def comb(n, r):
            r = min(r, n - r)
            res = 1
            for i in range(1, r + 1):
                res = res * (n - i + 1) // i
                if res >= LIMIT:
                    return LIMIT
            return res

        if count_perm(cnt, m) < k:
            return ""

        left = []

        for _ in range(m):
            for c in range(26):
                if cnt[c] == 0:
                    continue

                cnt[c] -= 1
                ways = count_perm(cnt, m - len(left) - 1)

                if ways >= k:
                    left.append(chr(c + 97))
                    break

                k -= ways
                cnt[c] += 1

        left = "".join(left)

        if len(s) % 2:
            return left + s[len(s) // 2] + left[::-1]

        return left + left[::-1]