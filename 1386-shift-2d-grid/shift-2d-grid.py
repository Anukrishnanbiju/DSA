class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        arr = []

        for row in grid:
            arr += row

        k %= m * n

        arr = arr[-k:] + arr[:-k]

        ans = []

        for i in range(m):
            ans.append(arr[i * n:(i + 1) * n])

        return ans