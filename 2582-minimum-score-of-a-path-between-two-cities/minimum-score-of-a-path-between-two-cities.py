from collections import deque

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = [[] for _ in range(n + 1)]

        for a, b, w in roads:
            g[a].append((b, w))
            g[b].append((a, w))

        q = deque([1])
        seen = {1}
        ans = float('inf')

        while q:
            u = q.popleft()

            for v, w in g[u]:
                ans = min(ans, w)

                if v not in seen:
                    seen.add(v)
                    q.append(v)

        return ans