class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dirs = (0, 1, 0, -1, 0)
        obs = {(x, y) for x, y in obstacles}

        x = y = 0
        d = 0
        ans = 0

        for c in commands:
            if c == -1:
                d = (d + 1) % 4

            elif c == -2:
                d = (d + 3) % 4

            else:
                for _ in range(c):
                    nx = x + dirs[d]
                    ny = y + dirs[d + 1]

                    if (nx, ny) in obs:
                        break

                    x, y = nx, ny
                    ans = max(ans, x * x + y * y)

        return ans