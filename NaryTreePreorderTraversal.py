from queue import *
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        answer = []
        
        if not root:
            return answer 
        
        def dfs(node):
            
            answer.append(node.val)
            
            for child in node.children:
                dfs(child)
        
        dfs(root)
        
        return answer
