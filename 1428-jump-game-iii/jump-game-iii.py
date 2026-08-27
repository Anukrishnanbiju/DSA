from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = deque([start])
        visited = [False] * len(arr)
        visited[start] = True

        while q:
            i = q.popleft()

            if arr[i] == 0:
                return True

            for j in (i + arr[i], i - arr[i]):
                if 0 <= j < len(arr) and not visited[j]:
                    visited[j] = True
                    q.append(j)

        return False