class Solution:
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        def calc(a, d, b, e):
            first = min(x + y for x, y in zip(a, d))
            return min(max(first, x) + y for x, y in zip(b, e))

        return min(
            calc(landStartTime, landDuration, waterStartTime, waterDuration),
            calc(waterStartTime, waterDuration, landStartTime, landDuration)
        )