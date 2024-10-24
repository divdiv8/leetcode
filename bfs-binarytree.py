#Given a binary tree, print its level wise traversal from left to right
#Input: root = [1,2,3,4,5,6,7]

#Output: [[1],[2,3],[4,5,6,7]]
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional
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
    
if __name__=="__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    solution = Solution()
    print(solution.levelOrder(root))