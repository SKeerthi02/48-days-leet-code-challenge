class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        if not root:
            return 
        def dfs(node):
            node.left , node.right = node.right, node.left 
        
            self.invertTree(node.left)
            self.invertTree(node.right)
        dfs(root)
        return root
