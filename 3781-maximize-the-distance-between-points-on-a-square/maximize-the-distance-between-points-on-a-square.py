from bisect import bisect_left

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        P = 4 * side

        def pos(x, y):
            if x == 0:
                return y
            if y == side:
                return side + x
            if x == side:
                return 3 * side - y
            return P - x

        a = sorted(pos(x, y) for x, y in points)
        n = len(a)

        def check(d):
            b = a + [x + P for x in a]

            for start in range(n):
                cur = start
                last = a[start]

                for _ in range(k - 1):
                    cur = bisect_left(b, last + d, cur + 1)

                    if cur >= start + n:
                        break

                    last = b[cur]

                else:
                    if b[cur] - a[start] <= P - d:
                        return True

            return False

        lo, hi = 0, side

        while lo < hi:
            mid = (lo + hi + 1) // 2

            if check(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo