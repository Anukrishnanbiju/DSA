class Node:
    def __init__(self, l, r, s):
        self.l = l
        self.r = r
        self.left = self.right = None

        if l == r:
            self.leftChar = self.rightChar = s[l]
            self.leftLen = self.rightLen = self.best = 1
        else:
            m = (l + r) // 2
            self.left = Node(l, m, s)
            self.right = Node(m + 1, r, s)
            self.pull()

    def pull(self):
        a, b = self.left, self.right

        self.leftChar = a.leftChar
        self.rightChar = b.rightChar

        self.leftLen = a.leftLen
        if a.leftLen == a.r - a.l + 1 and a.rightChar == b.leftChar:
            self.leftLen += b.leftLen

        self.rightLen = b.rightLen
        if b.rightLen == b.r - b.l + 1 and a.rightChar == b.leftChar:
            self.rightLen += a.rightLen

        self.best = max(a.best, b.best)

        if a.rightChar == b.leftChar:
            self.best = max(self.best, a.rightLen + b.leftLen)


class Solution:
    def longestRepeating(self, s: str, queryCharacters, queryIndices):
        n = len(s)
        root = Node(0, n - 1, s)
        ans = []

        def update(node, pos, ch):
            if node.l == node.r:
                node.leftChar = node.rightChar = ch
                return

            if pos <= node.left.r:
                update(node.left, pos, ch)
            else:
                update(node.right, pos, ch)

            node.pull()

        for ch, pos in zip(queryCharacters, queryIndices):
            update(root, pos, ch)
            ans.append(root.best)

        return ans        