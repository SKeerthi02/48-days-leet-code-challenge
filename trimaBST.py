class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        
        def dfs(node):
            if not node:
                return None
            elif node.val < L:
                return dfs(node.right)
            elif node.val > R:
                return dfs(node.left)
            else:
                node.left = dfs(node.left)
                node.right = dfs(node.right)
                return node
        
        
        return dfs(root)
