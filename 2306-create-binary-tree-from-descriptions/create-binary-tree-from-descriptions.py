class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        child = set()

        for p, c, left in descriptions:
            if p not in nodes:
                nodes[p] = TreeNode(p)
            if c not in nodes:
                nodes[c] = TreeNode(c)

            if left:
                nodes[p].left = nodes[c]
            else:
                nodes[p].right = nodes[c]

            child.add(c)

        for x in nodes:
            if x not in child:
                return nodes[x]