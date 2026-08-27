class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        left = sorted(s[:n // 2])

        a = ''.join(left)

        if n % 2:
            return a + s[n // 2] + a[::-1]

        return a + a[::-1]