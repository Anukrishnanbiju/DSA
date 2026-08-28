class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26

        for c in s:
            cnt[ord(c) - 97] += 1

        if sum(x % 2 for x in cnt) > 1:
            return ""

        mid = -1

        if len(s) % 2:
            for i in range(26):
                if cnt[i] % 2:
                    mid = i
                    cnt[i] -= 1
                    break

        half = []
        n = len(s)

        # Try to keep the left half equal to target
        for i in range(n // 2):
            x = ord(target[i]) - 97

            cnt[x] -= 2
            half.append(target[i])

            if cnt[x] < 0:
                break

        else:
            left = ''.join(half)

            if n % 2:
                candidate = left + chr(97 + mid) + left[::-1]
            else:
                candidate = left + left[::-1]

            if candidate > target:
                return candidate

        # Backtrack from the right
        while half:
            x = ord(half.pop()) - 97
            cnt[x] += 2

            # Put a slightly larger character here
            for y in range(x + 1, 26):
                if cnt[y] < 2:
                    continue

                cnt[y] -= 2
                half.append(chr(97 + y))

                # Fill the remaining half with smallest characters
                for z in range(26):
                    while cnt[z] >= 2:
                        cnt[z] -= 2
                        half.append(chr(97 + z))

                left = ''.join(half)

                if n % 2:
                    return left + chr(97 + mid) + left[::-1]
                else:
                    return left + left[::-1]

        return ""