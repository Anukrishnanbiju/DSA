class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = ""

        for word in words:
            s = sum(weights[ord(c) - 97] for c in word)
            ans += chr(122 - s % 26)

        return ans