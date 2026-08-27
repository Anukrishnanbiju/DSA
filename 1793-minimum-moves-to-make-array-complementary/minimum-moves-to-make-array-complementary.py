class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        diff = [0] * (2 * limit + 2)
        n = len(nums)

        for i in range(n // 2):
            a = nums[i]
            b = nums[n - 1 - i]

            x = min(a, b)
            y = max(a, b)

            diff[2] += 2
            diff[x + 1] -= 1
            diff[x + y] -= 1
            diff[x + y + 1] += 1
            diff[y + limit + 1] += 1

        ans = n
        moves = 0

        for s in range(2, 2 * limit + 1):
            moves += diff[s]
            ans = min(ans, moves)

        return ans