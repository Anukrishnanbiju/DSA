class Solution:
    def checkDivisibility(self, n: int) -> bool:
        original = n
        s = 0
        p = 1

        while n:
            n, d = divmod(n, 10)
            s += d
            p *= d

        return original % (s + p) == 0
                