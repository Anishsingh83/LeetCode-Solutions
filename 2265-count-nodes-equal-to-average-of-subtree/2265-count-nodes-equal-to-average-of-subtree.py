# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count = 0

        def dfs(node):
            nonlocal count
            if not node:
                return 0, 0
            
            left_sum, left_nodes = dfs(node.left)
            right_sum, right_nodes = dfs(node.right)
            
            total_sum = left_sum + right_sum + node.val
            total_nodes = left_nodes + right_nodes + 1
            
            if total_sum // total_nodes == node.val:
                count += 1
                
            return total_sum, total_nodes

        dfs(root)
        return count