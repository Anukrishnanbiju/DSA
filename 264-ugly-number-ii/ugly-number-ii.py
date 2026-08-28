class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1] * n

        p2 = p3 = p5 = 0

        for i in range(1, n):
            a = ugly[p2] * 2
            b = ugly[p3] * 3
            c = ugly[p5] * 5

            ugly[i] = min(a, b, c)

            if ugly[i] == a:
                p2 += 1

            if ugly[i] == b:
                p3 += 1

            if ugly[i] == c:
                p5 += 1

        return ugly[-1]