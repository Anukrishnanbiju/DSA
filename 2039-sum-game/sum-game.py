class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        a = num[:n//2]
        b = num[n//2:]

        s1 = sum(int(x) for x in a if x != '?')
        s2 = sum(int(x) for x in b if x != '?')

        q1 = a.count('?')
        q2 = b.count('?')

        return (q1 + q2) % 2 == 1 or s1 - s2 != 9 * (q2 - q1) // 2