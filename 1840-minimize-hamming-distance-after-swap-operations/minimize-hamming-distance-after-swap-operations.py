from collections import defaultdict, Counter

class Solution:
    def minimumHammingDistance(self, source, target, allowedSwaps):
        n = len(source)
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            a = find(a)
            b = find(b)
            if a != b:
                parent[b] = a

        for a, b in allowedSwaps:
            union(a, b)

        groups = defaultdict(Counter)

        for i in range(n):
            groups[find(i)][source[i]] += 1

        ans = 0

        for i in range(n):
            root = find(i)

            if groups[root][target[i]] > 0:
                groups[root][target[i]] -= 1
            else:
                ans += 1

        return ans