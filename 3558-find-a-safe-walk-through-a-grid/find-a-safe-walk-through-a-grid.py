from collections import deque

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        best = [[-1] * n for _ in range(m)]
        
        health -= grid[0][0]
        best[0][0] = health
        
        q = deque([(0, 0, health)])
        d = [(1,0),(-1,0),(0,1),(0,-1)]
        
        while q:
            i, j, h = q.popleft()
            
            if i == m - 1 and j == n - 1:
                return True
            
            for di, dj in d:
                x, y = i + di, j + dj
                
                if 0 <= x < m and 0 <= y < n:
                    nh = h - grid[x][y]
                    
                    if nh > 0 and nh > best[x][y]:
                        best[x][y] = nh
                        q.append((x, y, nh))
        
        return False