class Solution:
    def processStr(self, s: str, k: int) -> str:
        length = 0

        for c in s:
            if c == '*':
                length = max(0, length - 1)
            elif c == '#':
                length *= 2
            elif c != '%':
                length += 1

        if k >= length:
            return '.'

        for c in s[::-1]:
            if c == '*':
                length += 1
            elif c == '#':
                length //= 2
                if k >= length:
                    k -= length
            elif c == '%':
                k = length - 1 - k
            else:
                length -= 1
                if k == length:
                    return c

        return '.'