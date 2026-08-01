from functools import cache

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        @cache
        def dp(l, r):
            if l == r:
                return nums[l]

            left = nums[l] - dp(l + 1, r)
            right = nums[r] - dp(l, r - 1)

            return max(left, right)

        return dp(0, len(nums) - 1) >= 0  