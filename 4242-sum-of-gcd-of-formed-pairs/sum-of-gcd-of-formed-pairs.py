from math import gcd

class Solution:
    def gcdSum(self, nums: List[int]) -> int:
        n = len(nums)
        arr = []
        mx = 0

        for x in nums:
            mx = max(mx, x)
            arr.append(gcd(x, mx))

        arr.sort()

        ans = 0

        for i in range(n // 2):
            ans += gcd(arr[i], arr[n - 1 - i])

        return ans