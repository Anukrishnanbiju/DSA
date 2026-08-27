class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        x = 0

        for n in arr:
            x = min(x + 1, n)

        return x