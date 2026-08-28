class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        i = 0

        while i < len(words):
            j = i
            letters = 0

            # Find words for this line
            while j < len(words) and letters + len(words[j]) + (j - i) <= maxWidth:
                letters += len(words[j])
                j += 1

            count = j - i
            gaps = count - 1

            # Last line or single word
            if j == len(words) or count == 1:
                line = " ".join(words[i:j])
                ans.append(line + " " * (maxWidth - len(line)))

            else:
                spaces = maxWidth - letters
                each, extra = divmod(spaces, gaps)

                line = ""

                for k in range(i, j - 1):
                    line += words[k]
                    line += " " * (each + (1 if k - i < extra else 0))

                line += words[j - 1]
                ans.append(line)

            i = j

        return ans