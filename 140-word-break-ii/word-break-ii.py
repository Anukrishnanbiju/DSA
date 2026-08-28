class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        memo = {}

        def dfs(i):
            if i == len(s):
                return [""]

            if i in memo:
                return memo[i]

            res = []

            for j in range(i + 1, len(s) + 1):
                word = s[i:j]

                if word not in words:
                    continue

                for tail in dfs(j):
                    if tail:
                        res.append(word + " " + tail)
                    else:
                        res.append(word)

            memo[i] = res
            return res

        return dfs(0)