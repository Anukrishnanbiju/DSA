from collections import deque

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        d = {
            1: [(0,-1), (0,1)],
            2: [(-1,0), (1,0)],
            3: [(0,-1), (1,0)],
            4: [(0,1), (1,0)],
            5: [(0,-1), (-1,0)],
            6: [(0,1), (-1,0)]
        }

        q = deque([(0, 0)])
        seen = {(0, 0)}

        while q:
            r, c = q.popleft()

            if r == m - 1 and c == n - 1:
                return True

            for dr, dc in d[grid[r][c]]:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                if (nr, nc) in seen:
                    continue

                if (-dr, -dc) in d[grid[nr][nc]]:
                    seen.add((nr, nc))
                    q.append((nr, nc))

        return False