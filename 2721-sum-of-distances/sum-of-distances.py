from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        pos = defaultdict(list)

        for i, x in enumerate(nums):
            pos[x].append(i)

        ans = [0] * len(nums)

        for a in pos.values():
            m = len(a)

            left = 0
            right = sum(a) - m * a[0]

            for i in range(m):
                ans[a[i]] = left + right

                if i + 1 < m:
                    d = a[i + 1] - a[i]

                    left += d * (i + 1)
                    right -= d * (m - i - 1)

        return ans