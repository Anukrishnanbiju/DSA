class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m = len(boxGrid)
        n = len(boxGrid[0])

        for r in range(m):
            pos = n - 1

            for c in range(n - 1, -1, -1):
                if boxGrid[r][c] == '*':
                    pos = c - 1
                elif boxGrid[r][c] == '#':
                    boxGrid[r][c] = '.'
                    boxGrid[r][pos] = '#'
                    pos -= 1

        ans = [['.'] * m for _ in range(n)]

        for r in range(m):
            for c in range(n):
                ans[c][m - 1 - r] = boxGrid[r][c]

        return ans