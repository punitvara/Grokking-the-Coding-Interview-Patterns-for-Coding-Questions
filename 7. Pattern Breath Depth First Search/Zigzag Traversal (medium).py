'''
Problem Statement
Given a binary tree, populate an array to represent its zigzag level order traversal.
You should populate the values of all nodes of the first level from left to right,
then right to left for the next level and keep alternating in the same manner for the following levels.

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Input: root = [3,9,20,1,2,15,7]
Output: [[3],[20,9],[1,2,15,7]]
'''

# mycode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        final_list = []
        if not root:
            return final_list

        q = deque()
        q.append(root)
        # when this flag is true, append nodes normally right side/at the end of second queue
        left_to_right = True
        while q:
            queue_length = len(q)
            # save current list in queue instead of list
            current_list =  deque()
            for _ in range(queue_length):
                element = q.popleft()
                # if flag is true then add nodes values as it is otherwise add in reverse in leftappend for queue
                if left_to_right:
                    current_list.append(element.val)
                else:
                    current_list.appendleft(element.val)

                if element.left:
                    q.append(element.left)
                if element.right:
                    q.append(element.right)
            # Change flag after each iteration
            left_to_right = not left_to_right

            final_list.append(current_list)
        return final_list

#answer
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def traverse(root):
  result = []
  if root is None:
    return result

  queue = deque()
  queue.append(root)
  leftToRight = True
  while queue:
    levelSize = len(queue)
    currentLevel = deque()
    for _ in range(levelSize):
      currentNode = queue.popleft()

      # add the node to the current level based on the traverse direction
      if leftToRight:
        currentLevel.append(currentNode.val)
      else:
        currentLevel.appendleft(currentNode.val)

      # insert the children of current node in the queue
      if currentNode.left:
        queue.append(currentNode.left)
      if currentNode.right:
        queue.append(currentNode.right)

    result.append(list(currentLevel))
    # reverse the traversal direction
    leftToRight = not leftToRight

  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.right.left.left = TreeNode(20)
  root.right.left.right = TreeNode(17)
  print("Zigzag traversal: " + str(traverse(root)))


main()


'''
Time complexity
The time complexity of the above algorithm is O(N), where ‘N’ is the total number of nodes in the tree.
This is due to the fact that we traverse each node once.
Space complexity
The space complexity of the above algorithm will be O(N) as we need to return a list containing the level order traversal.
We will also need O(N) space for the queue. Since we can have a maximum of N/2 nodes at any level (this could happen only at the lowest level),
therefore we will need O(N) space to store them in the queue.
'''
