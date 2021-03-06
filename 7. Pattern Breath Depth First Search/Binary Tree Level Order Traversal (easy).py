'''
Problem Statement
Given a binary tree, populate an array to represent its level-by-level traversal.
You should populate the values of all nodes of each level from left to right in separate sub-arrays.
'''

'''
1. Add root to queue
2. Traverse until queue is not empty
3  Check level by checking length of queue.
4. Loop until queue length is zero
5. popleft element from queue and add to current list
6. add left and right node if available.
7. After each for loop add current list to final list. Each represent nodes of current level.
8. Return final list which is list of list.
'''
# my answer (Limit exceeded on LC)
from collections import deque
class Solution:

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        final_list = []
        if not root: return final_list
        q = deque()
        q.append(root)
        while q:
            print (q)
            levelsize = len(q)
            # print (levelsize)
            current_list = []
            for i in range(levelsize):
                element = q.popleft()
                current_list.append(element.val)

                if element.left:
                    q.append(element.left)
                if element.right:
                    q.append(element.right)
            final_list.append(current_list)
        return final_list

# My answer 2
from collections import deque
class Solution:

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        final_list = []
        if not root: return final_list
        q = deque()
        q.append(root)
        level = 0
        # Traverse until queue is empty
        while q:
            queue_length = len(q)
            final_list.append([])
            for _ in range(queue_length):
                # add new empty list end of final list to fill current level elements
                element = q.popleft()
                final_list[level].append(element.val)

                if element.left:
                    q.append(element.left)
                if element.right:
                    q.append(element.right)
            level += 1
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
  while queue:
    levelSize = len(queue)
    currentLevel = []
    for _ in range(levelSize):
      currentNode = queue.popleft()
      # add the node to the current level
      currentLevel.append(currentNode.val)
      # insert the children of current node in the queue
      if currentNode.left:
        queue.append(currentNode.left)
      if currentNode.right:
        queue.append(currentNode.right)

    result.append(currentLevel)

  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level order traversal: " + str(traverse(root)))


main()


'''
Time complexity
The time complexity of the above algorithm is O(N), where ???N??? is the total number of nodes in the tree.
This is due to the fact that we traverse each node once.
Space complexity
The space complexity of the above algorithm will be O(N) as we need to return a list containing the level order traversal.
We will also need O(N) space for the queue. Since we can have a maximum of N/2 nodes at any level (this could happen only at the lowest level),
therefore we will need O(N) space to store them in the queue.
'''
