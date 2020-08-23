class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.count = 0
        
        def dfs(node, tempCount):
            
            if not node:
                return 0
            self.count = max(self.count, tempCount)
            for child in node.children:
                dfs(child, tempCount+1)
                
        
        dfs(root, 1)
        return self.count
