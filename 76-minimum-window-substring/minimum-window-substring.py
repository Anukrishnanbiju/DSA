from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)

        left = 0
        start = 0
        best = float("inf")

        for right in range(len(s)):
            if need[s[right]] > 0:
                missing -= 1

            need[s[right]] -= 1

            while missing == 0:
                if right - left + 1 < best:
                    best = right - left + 1
                    start = left

                need[s[left]] += 1

                if need[s[left]] > 0:
                    missing += 1

                left += 1

        return "" if best == float("inf") else s[start:start + best]