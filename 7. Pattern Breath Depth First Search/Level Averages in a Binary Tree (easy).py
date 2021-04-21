'''
Problem Statement
Given a binary tree, populate an array to represent the averages of all of its levels.
Input: root = [3,9,20,null,15,7]
Output: [3.00000,14.50000,11.00000]
'''

# my amswer
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        final_list = []
        if not root:
            return final_list
        q = deque()
        q.append(root)
        while q:
            queue_length = len(q)
            current_list = []
            for _ in range(queue_length):
                element = q.popleft()
                current_list.append(element.val)
                if element.left:
                    q.append(element.left)
                if element.right:
                    q.append(element.right)
            final_list.append(mean(current_list))
        return final_list


#answer
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_level_averages(root):
  result = []
  if root is None:
    return result

  queue = deque()
  queue.append(root)
  while queue:
    levelSize = len(queue)
    levelSum = 0.0
    for _ in range(levelSize):
      currentNode = queue.popleft()
      # add the node's value to the running sum
      levelSum += currentNode.val
      # insert the children of current node to the queue
      if currentNode.left:
        queue.append(currentNode.left)
      if currentNode.right:
        queue.append(currentNode.right)

    # append the current level's average to the result array
    result.append(levelSum / levelSize)

  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.left.right = TreeNode(2)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level averages are: " + str(find_level_averages(root)))


main()


'''
Time complexity
The time complexity of the above algorithm is O(N), where ‘N’ is the total number of nodes in the tree.
This is due to the fact that we traverse each node once.
Space complexity
The space complexity of the above algorithm will be O(N)O which is required for the queue.
Since we can have a maximum of N/2 nodes at any level (this could happen only at the lowest level),
therefore we will need O(N) space to store them in the queue.
'''
