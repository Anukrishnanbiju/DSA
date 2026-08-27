class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        h = ans = 0

        for x in gain:
            h += x
            ans = max(ans, h)

        return ans