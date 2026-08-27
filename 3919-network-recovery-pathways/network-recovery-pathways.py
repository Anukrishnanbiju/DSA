class Solution:
    def findMaxPathScore(self, edges, online, k):
        n = len(online)
        g = [[] for _ in range(n)]
        indeg = [0] * n
        lo = 10**18
        hi = 0

        for u, v, w in edges:
            if online[u] and online[v]:
                g[u].append((v, w))
                indeg[v] += 1
                lo = min(lo, w)
                hi = max(hi, w)

        if lo == 10**18:
            return -1

        order = []
        q = [i for i in range(n) if indeg[i] == 0]

        for u in q:
            order.append(u)
            for v, w in g[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        def check(x):
            inf = 10**30
            dp = [inf] * n
            dp[0] = 0

            for u in order:
                if dp[u] > k:
                    continue

                for v, w in g[u]:
                    if w >= x:
                        dp[v] = min(dp[v], dp[u] + w)

            return dp[n - 1] <= k

        if not check(lo):
            return -1

        while lo < hi:
            mid = (lo + hi + 1) // 2
            if check(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo