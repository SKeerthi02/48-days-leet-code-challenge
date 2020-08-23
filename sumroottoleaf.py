class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.answer = 0
        
        def dfs(node, path):
            
            if node:
                path = (path << 1) | node.val
                
                if not (node.left or node.right):
                    self.answer += path
                dfs(node.left, path)
                dfs(node.right, path)
            
            
        dfs(root, 0)
        return self.answer
