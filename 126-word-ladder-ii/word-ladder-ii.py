from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        words = set(wordList)

        if endWord not in words:
            return []

        parents = defaultdict(list)
        q = deque([beginWord])
        words.discard(beginWord)
        found = False

        while q and not found:
            nxt = set()

            for _ in range(len(q)):
                word = q.popleft()

                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c == word[i]:
                            continue

                        new = word[:i] + c + word[i+1:]

                        if new in words:
                            parents[new].append(word)
                            nxt.add(new)

                            if new == endWord:
                                found = True

            words -= nxt
            q.extend(nxt)

        if not found:
            return []

        ans = []
        path = [endWord]

        def dfs(word):
            if word == beginWord:
                ans.append(path[::-1])
                return

            for p in parents[word]:
                path.append(p)
                dfs(p)
                path.pop()

        dfs(endWord)
        return ans