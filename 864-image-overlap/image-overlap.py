class Solution:
    def largestOverlap(self, img1, img2):
        n = len(img1)
        ans = 0

        for dx in range(-n + 1, n):
            for dy in range(-n + 1, n):
                count = 0

                for i in range(n):
                    for j in range(n):
                        x, y = i + dx, j + dy

                        if 0 <= x < n and 0 <= y < n:
                            if img1[i][j] == img2[x][y] == 1:
                                count += 1

                ans = max(ans, count)

        return ans