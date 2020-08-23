class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.length = 0
        
        def dfs(node, depth):
            if not node:
                return 0
            if node:
                left = dfs(node.left, depth+1)
                right = dfs(node.right, depth+ 1)
            
            self.length = max(self.length, left+right)
            return max(left, right) + 1
            
        dfs(root, 0)
        return self.length
