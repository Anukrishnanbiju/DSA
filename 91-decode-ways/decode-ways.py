class Solution:
    def numDecodings(self, s):
        a, b = 1, 0

        for i in range(len(s) - 1, -1, -1):
            cur = 0

            if s[i] != '0':
                cur = a

                if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                    cur += b

            b = a
            a = cur

        return a