from functools import lru_cache

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)

        @lru_cache(None)
        def dfs(i):
            ans = 1

            for j in range(i - 1, max(-1, i - d - 1), -1):
                if arr[j] >= arr[i]:
                    break
                ans = max(ans, 1 + dfs(j))

            for j in range(i + 1, min(n, i + d + 1)):
                if arr[j] >= arr[i]:
                    break
                ans = max(ans, 1 + dfs(j))

            return ans

        return max(dfs(i) for i in range(n))