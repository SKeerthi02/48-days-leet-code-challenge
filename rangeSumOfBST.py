class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        
        self.totalSum = 0
        
        def dfs(node, L, R):
            if node:
                if node.val >= L and node.val <= R:
                    self.totalSum += node.val
                dfs(node.left, L, R)
                dfs(node.right, L ,R)
        
        dfs(root, L, R)
        return self.totalSum
