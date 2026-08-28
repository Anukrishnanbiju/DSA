class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = [v for row in grid for v in row]

        r = nums[0] % x

        for v in nums:
            if v % x != r:
                return -1

        nums.sort()
        mid = nums[len(nums) // 2]

        return sum(abs(v - mid) // x for v in nums)