from collections import deque

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        seen = [[False] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                if seen[r][c]:
                    continue

                seen[r][c] = True
                q = deque([(r, c, -1, -1)])

                while q:
                    x, y, px, py = q.popleft()

                    for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
                        nx, ny = x + dx, y + dy

                        if not (0 <= nx < m and 0 <= ny < n):
                            continue

                        if grid[nx][ny] != grid[x][y]:
                            continue

                        if nx == px and ny == py:
                            continue

                        if seen[nx][ny]:
                            return True

                        seen[nx][ny] = True
                        q.append((nx, ny, x, y))

        return False