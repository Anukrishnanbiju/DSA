from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []

        for i, x in enumerate(nums):

            # Remove elements outside the window
            while q and q[0] <= i - k:
                q.popleft()

            # Remove smaller elements
            while q and nums[q[-1]] <= x:
                q.pop()

            q.append(i)

            # Window is ready
            if i >= k - 1:
                ans.append(nums[q[0]])

        return ans