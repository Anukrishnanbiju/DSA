from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        words = set(wordList)

        if endWord not in words:
            return 0

        q = deque([(beginWord, 1)])

        while q:
            word, steps = q.popleft()

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    new = word[:i] + c + word[i+1:]

                    if new == endWord:
                        return steps + 1

                    if new in words:
                        words.remove(new)
                        q.append((new, steps + 1))

        return 0