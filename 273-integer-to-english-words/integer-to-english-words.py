class Solution:
    def numberToWords(self, num: int) -> str:
        one = [
            "", "One", "Two", "Three", "Four", "Five", "Six",
            "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
            "Thirteen", "Fourteen", "Fifteen", "Sixteen",
            "Seventeen", "Eighteen", "Nineteen"
        ]

        ten = [
            "", "", "Twenty", "Thirty", "Forty", "Fifty",
            "Sixty", "Seventy", "Eighty", "Ninety"
        ]

        def helper(n):
            if n == 0:
                return ""
            if n < 20:
                return one[n]
            if n < 100:
                return ten[n // 10] + " " + helper(n % 10)
            return one[n // 100] + " Hundred " + helper(n % 100)

        if num == 0:
            return "Zero"

        ans = []

        if num >= 1_000_000_000:
            ans.append(helper(num // 1_000_000_000) + " Billion")
            num %= 1_000_000_000

        if num >= 1_000_000:
            ans.append(helper(num // 1_000_000) + " Million")
            num %= 1_000_000

        if num >= 1000:
            ans.append(helper(num // 1000) + " Thousand")
            num %= 1000

        if num > 0:
            ans.append(helper(num))

        return " ".join(ans).replace("  ", " ").strip()