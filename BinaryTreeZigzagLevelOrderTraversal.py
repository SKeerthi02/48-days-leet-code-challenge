

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        answer = []
        level = deque()
        
        if not root:
            return answer
        
        tree_node_que = deque([root, None])
        
        is_left = True
        
        while len(tree_node_que) > 0:
            
            node = tree_node_que.popleft()
            
            if node:
                
                if is_left:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                
                if node.left:
                    tree_node_que.append(node.left)
                if node.right:
                    tree_node_que.append(node.right)
            else:
                
                answer.append(level)
                
                if len(tree_node_que) > 0:
                    tree_node_que.append(None)
                level = deque()
                
                is_left = not is_left
                        
        return answer  
