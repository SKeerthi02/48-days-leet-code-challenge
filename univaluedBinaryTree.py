class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        
        val = root.val
        self.flag = True
        def dfs(node):
            if node.val != val:
                self.flag = False
                return False
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        
        dfs(root)
        return self.flag
