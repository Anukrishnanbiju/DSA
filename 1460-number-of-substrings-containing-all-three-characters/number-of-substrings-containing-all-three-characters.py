class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        a = b = c = -1
        ans = 0

        for i, x in enumerate(s):
            if x == 'a':
                a = i
            elif x == 'b':
                b = i
            else:
                c = i

            ans += min(a, b, c) + 1

        return ans