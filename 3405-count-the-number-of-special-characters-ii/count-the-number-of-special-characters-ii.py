class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        last = [-1] * 26
        first = [len(word)] * 26

        for i, c in enumerate(word):
            if c.islower():
                last[ord(c) - 97] = i
            else:
                first[ord(c) - 65] = min(first[ord(c) - 65], i)

        return sum(last[i] < first[i] for i in range(26) if last[i] != -1 and first[i] != len(word))