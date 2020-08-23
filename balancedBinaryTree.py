class Solution:
    
    def dfs(self, node):
        if not node:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        return 1 + max(left, right)
            
    def isBalanced(self, root: TreeNode) -> bool:
        
        if not root:
            return True
            
        return abs(self.dfs(root.left) - self.dfs(root.right)) < 2 and self.isBalanced(root.right) and self.isBalanced(root.left)
