class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        pos = {}
        ans = len(nums) + 1

        def rev(x):
            r = 0
            while x:
                r = r * 10 + x % 10
                x //= 10
            return r

        for i, x in enumerate(nums):
            if x in pos:
                ans = min(ans, i - pos[x])

            pos[rev(x)] = i

        return -1 if ans == len(nums) + 1 else ans