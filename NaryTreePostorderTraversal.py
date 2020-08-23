class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        if not root: return []
        
        stack, answer = [root, ], []
        
        while stack:
            node = stack.pop()
            
            if node:
                answer.append(node.val)
            
            for child in node.children:
                stack.append(child)
            
        return answer[::-1]
