class Solution:
    def countDigitOne(self, n: int) -> int:
        ans = 0
        place = 1

        while place <= n:
            high = n // (place * 10)
            cur = (n // place) % 10
            low = n % place

            ans += high * place

            if cur == 1:
                ans += low + 1
            elif cur > 1:
                ans += place

            place *= 10

        return ans