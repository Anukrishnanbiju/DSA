from collections import Counter

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        count = Counter(nums)

        if k == len(nums):
            return max(nums)

        if k == 1:
            return max((x for x in nums if count[x] == 1), default=-1)

        return max(
            nums[0] if count[nums[0]] == 1 else -1,
            nums[-1] if count[nums[-1]] == 1 else -1
        )