'''
Problem Challenge 2
Right View of a Binary Tree (easy)
Given a binary tree, return an array containing nodes in its right view.
The right view of a binary tree is the set of nodes visible when the tree is seen from the right side.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        final_list = []
        if not root:
            return final_list
        q = deque()
        q.append(root)
        while q:
            queue_length = len(q)

            for _ in range(queue_length):
                element = q.popleft()
                last_number = element.val
                if element.left:
                    q.append(element.left)
                if element.right:
                    q.append(element.right)
            final_list.append(last_number)
        return final_list

        #answer
        from __future__ import print_function
        from collections import deque


        class TreeNode:
          def __init__(self, val):
            self.val = val
            self.left, self.right = None, None


        def tree_right_view(root):
          result = []
          if root is None:
            return result

          queue = deque()
          queue.append(root)
          while queue:
            levelSize = len(queue)
            for i in range(0, levelSize):
              currentNode = queue.popleft()
              # if it is the last node of this level, add it to the result
              if i == levelSize - 1:
                result.append(currentNode)
              # insert the children of current node in the queue
              if currentNode.left:
                queue.append(currentNode.left)
              if currentNode.right:
                queue.append(currentNode.right)

          return result


        def main():
          root = TreeNode(12)
          root.left = TreeNode(7)
          root.right = TreeNode(1)
          root.left.left = TreeNode(9)
          root.right.left = TreeNode(10)
          root.right.right = TreeNode(5)
          root.left.left.left = TreeNode(3)
          result = tree_right_view(root)
          print("Tree right view: ")
          for node in result:
            print(str(node.val) + " ", end='')


        main()



        '''
        Time complexity #
        The time complexity of the above algorithm is O(N), where ‘N’ is the total number of nodes in the tree.
        This is due to the fact that we traverse each node once.
        Space complexity
        The space complexity of the above algorithm will be O(N) as we need to return a list containing the level order traversal.
        We will also need O(N) space for the queue. Since we can have a maximum of N/2 nodes at any level
        (this could happen only at the lowest level), therefore we will need O(N) space to store them in the queue.
        '''

        '''
        Similar Questions #
        Problem 1: Given a binary tree, return an array containing nodes in its left view.
        The left view of a binary tree is the set of nodes visible when the tree is seen from the left side.
        Solution: We will be following a similar approach,
        but instead of appending the last element of each level we will be appending the first element of each level to the output array.
        '''
