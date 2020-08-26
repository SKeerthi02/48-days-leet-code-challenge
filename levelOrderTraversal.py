class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        answer = []
        
        levels = 0
        if not root:
            return answer
        
        def bfs(node, levels):
            
            if len(answer) == levels:
                answer.append([])
            
            answer[levels].append(node.val)
            
            if node.left:
                bfs(node.left, levels+1)
            if node.right:
                bfs(node.right, levels+1)
            return 
        
        bfs(root, levels)
        
        return answer
