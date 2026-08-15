class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter

        need = Counter(words)
        n = len(words)
        size = len(words[0])
        ans = []

        for start in range(size):
            left = start
            right = start
            count = Counter()

            while right + size <= len(s):
                word = s[right:right + size]
                right += size

                if word not in need:
                    count.clear()
                    left = right
                    continue

                count[word] += 1

                while count[word] > need[word]:
                    remove = s[left:left + size]
                    count[remove] -= 1
                    left += size

                if right - left == n * size:
                    ans.append(left)

        return ans