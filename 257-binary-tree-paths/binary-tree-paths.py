class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        path = []

        def dfs(node):
            if not node:
                return

            path.append(str(node.val))

            if not node.left and not node.right:
                ans.append("->".join(path))
            else:
                dfs(node.left)
                dfs(node.right)

            path.pop()

        dfs(root)
        return ans