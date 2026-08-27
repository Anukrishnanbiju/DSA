class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 1000000007
        m = r - l + 1
        s = 2 * m

        a = [[0] * s for _ in range(s)]

        for i in range(m):
            for j in range(m):
                if j < i:
                    a[i][m + j] = 1
                elif j > i:
                    a[m + i][j] = 1

        def mul(A, B):
            C = [[0] * s for _ in range(s)]

            for i in range(s):
                for k in range(s):
                    if A[i][k]:
                        x = A[i][k]
                        for j in range(s):
                            if B[k][j]:
                                C[i][j] = (C[i][j] + x * B[k][j]) % MOD

            return C

        def mpow(A, e):
            R = [[0] * s for _ in range(s)]

            for i in range(s):
                R[i][i] = 1

            while e:
                if e & 1:
                    R = mul(R, A)
                A = mul(A, A)
                e >>= 1

            return R

        p = mpow(a, n - 1)

        ans = 0

        for i in range(s):
            for j in range(s):
                ans = (ans + p[i][j]) % MOD

        return ans