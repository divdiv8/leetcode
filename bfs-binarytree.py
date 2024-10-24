#Given a binary tree, print its level wise traversal from left to right
#Input: root = [1,2,3,4,5,6,7]

#Output: [[1],[2,3],[4,5,6,7]]
from typing import List, Optional
from collections import deque 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        def bfs(root,level):
            if not root:
                return
            if len(result) == level:
                result.append([])
        
            result[level].append(root.val)
            
            bfs(root.left,level+1)
            bfs(root.right,level+1)
        bfs(root,0)
        return result
    

    def levelOrder_iterative(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return []
        visited = deque()
        visited.append(root)
        
        while visited:
            val = []
            for i in range(len(visited)):
                node = visited.popleft()
                val.append(node.val)
                if node.left:
                    visited.append(node.left)
                if node.right:
                    visited.append(node.right)
            result.append(val)
        return result
        
        
if __name__=="__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    solution = Solution()

    print(solution.levelOrder(root))
    print(solution.levelOrder_iterative(root))

