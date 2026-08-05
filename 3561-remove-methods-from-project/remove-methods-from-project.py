from collections import defaultdict

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        rg = defaultdict(list)

        for u, v in invocations:
            g[u].append(v)
            rg[v].append(u)

        vis = set()

        def dfs(u):
            vis.add(u)
            for v in g[u]:
               if v not in vis:
                    dfs(v)


        dfs(k)

        for x in vis:
            for p in rg[x]:
                if p not in vis:
                    return list(range(n))

        return [i for i in range(n)if i not in vis]                                 