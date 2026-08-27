class Solution:
    def processStr(self, s: str) -> str:
        a = []

        for c in s:
            if 'a' <= c <= 'z':
                a.append(c)
            elif c == '*':
                if a:
                    a.pop()
            elif c == '#':
                a += a[:]
            else:
                a.reverse()

        return ''.join(a)