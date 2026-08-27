class Solution:
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        def calc(a, d, b, e):
            first = min(x + y for x, y in zip(a, d))
            ans = 10**18

            for x, y in zip(b, e):
                ans = min(ans, max(first, x) + y)

            return ans

        return min(
            calc(landStartTime, landDuration, waterStartTime, waterDuration),
            calc(waterStartTime, waterDuration, landStartTime, landDuration)
        )