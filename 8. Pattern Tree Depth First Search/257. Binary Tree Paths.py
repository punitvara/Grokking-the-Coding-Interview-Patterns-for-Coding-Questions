'''
Extra Problem
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.
'''

#mycode
class Solution:
    # def dfs(self, node: TreeNode, curr_path, all_path) -> List[str]:
    #     if not node:
    #         return []
    #     curr_path.append(node.val)
    #     if node.left is None and node.right is None:
    #         all_path.append(list(curr_path))
    #     self.dfs(node.left, curr_path, all_path)
    #     self.dfs(node.right, curr_path, all_path)
    #     del curr_path[-1]
    #     return all_path

    def dfs(self, node: TreeNode, curr_path, all_path) -> List[str]:
        if not node:
            return []
        curr_path.append(str(node.val))
        if node.left is None and node.right is None:
            all_path.append("->".join(curr_path))
        self.dfs(node.left, curr_path, all_path)
        self.dfs(node.right, curr_path, all_path)
        curr_path.pop()
        return all_path

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.curr_path = []
        self.all_path = []
        return self.dfs(root, self.curr_path, self.all_path)
