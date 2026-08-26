class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        n = len(matrix[0])
        h = [0] * n
        ans = 0

        for row in matrix:
            for i in range(n):
                h[i] = h[i] + 1 if row[i] == "1" else 0

            stack = [-1]

            for i in range(n + 1):
                x = h[i] if i < n else 0

                while stack[-1] != -1 and h[stack[-1]] > x:
                    height = h[stack.pop()]
                    width = i - stack[-1] - 1
                    ans = max(ans, height * width)

                stack.append(i)

        return ans