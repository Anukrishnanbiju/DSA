class Solution:
    def longestPalindrome(self, s):
        ans = ""

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]

        for i in range(len(s)):
            a = expand(i, i)
            b = expand(i, i + 1)

            if len(a) > len(ans):
                ans = a
            if len(b) > len(ans):
                ans = b

        return ans