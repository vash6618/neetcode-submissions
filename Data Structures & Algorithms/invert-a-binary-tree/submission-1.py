# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        bfs_queue = deque()
        if root:
            bfs_queue.append(root) 
        while(bfs_queue):
            node = bfs_queue.popleft()
            left = node.left
            if node.right:
                bfs_queue.append(node.right)
            if left:
                bfs_queue.append(left)
            node.left = node.right
            node.right = left
        return root



        