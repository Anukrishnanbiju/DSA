from math import gcd
from collections import defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        if n <= 2:
            return n

        ans = 1

        for i in range(n):
            x1, y1 = points[i]
            slopes = defaultdict(int)

            for j in range(i + 1, n):
                x2, y2 = points[j]

                dx = x2 - x1
                dy = y2 - y1

                g = gcd(dx, dy)
                dx //= g
                dy //= g

                # Normalize the direction
                if dx < 0:
                    dx = -dx
                    dy = -dy
                elif dx == 0:
                    dy = 1
                elif dy == 0:
                    dx = 1

                slopes[(dy, dx)] += 1
                ans = max(ans, slopes[(dy, dx)] + 1)

        return ans