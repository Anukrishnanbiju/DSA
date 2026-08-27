class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26

        for c in s:
            cnt[ord(c) - ord('a')] += 1

        n = len(s)

        # Try to match target from left to right
        i = 0
        while i < n:
            x = ord(target[i]) - ord('a')

            if cnt[x] == 0:
                break

            cnt[x] -= 1
            i += 1

        while i >= 0:

            # Try to make position i greater
            if i < n:
                x = ord(target[i]) - ord('a')

                for c in range(x + 1, 26):
                    if cnt[c] > 0:
                        cnt[c] -= 1

                        ans = target[:i] + chr(c + ord('a'))

                        # Fill remaining positions with smallest letters
                        for j in range(26):
                            ans += chr(j + ord('a')) * cnt[j]

                        return ans

            # Restore target[i] before moving left
            if i == 0:
                break

            i -= 1
            cnt[ord(target[i]) - ord('a')] += 1

        return ""