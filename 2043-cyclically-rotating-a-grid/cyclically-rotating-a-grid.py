class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        for layer in range(min(m, n) // 2):
            a = []

            for j in range(layer, n - layer - 1):
                a.append(grid[layer][j])

            for i in range(layer, m - layer - 1):
                a.append(grid[i][n - layer - 1])

            for j in range(n - layer - 1, layer, -1):
                a.append(grid[m - layer - 1][j])

            for i in range(m - layer - 1, layer, -1):
                a.append(grid[i][layer])

            k2 = k % len(a)
            a = a[k2:] + a[:k2]

            p = 0

            for j in range(layer, n - layer - 1):
                grid[layer][j] = a[p]
                p += 1

            for i in range(layer, m - layer - 1):
                grid[i][n - layer - 1] = a[p]
                p += 1

            for j in range(n - layer - 1, layer, -1):
                grid[m - layer - 1][j] = a[p]
                p += 1

            for i in range(m - layer - 1, layer, -1):
                grid[i][layer] = a[p]
                p += 1

        return grid