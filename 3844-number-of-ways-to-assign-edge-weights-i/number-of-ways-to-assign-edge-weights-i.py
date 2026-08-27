from collections import deque

class Solution:
    def assignEdgeWeights(self, edges):
        n = len(edges) + 1
        g = [[] for _ in range(n + 1)]

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        q = deque([1])
        seen = [False] * (n + 1)
        seen[1] = True
        depth = 0

        while q:
            for _ in range(len(q)):
                u = q.popleft()
                for v in g[u]:
                    if not seen[v]:
                        seen[v] = True
                        q.append(v)
            depth += 1

        return pow(2, depth - 2, 10**9 + 7)