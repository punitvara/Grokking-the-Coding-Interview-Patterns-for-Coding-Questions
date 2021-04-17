'''
Problem Challenge 2
Path with Maximum Sum (hard)
Find the path with the maximum sum in a given binary tree. Write a function that returns the maximum sum.
A path can be defined as a sequence of nodes between any two nodes and doesn’t necessarily pass through the root.
'''

# my answer:
class Solution:
    def __init__(self):
        self.M = -sys.maxsize-1
    def dfs(self, root:TreeNode) -> int:
        if not root:
            return 0
        l_sum = self.dfs(root.left)
        r_sum = self.dfs(root.right)

        # If both sum are less than 0, Ignore both
        if l_sum < 0 and r_sum < 0:
            Total = root.val
        # If left sum is less than 0, Ignore it
        elif l_sum < 0:
            Total = r_sum + root.val
        # If right sum is less than 0, Ignore it
        elif r_sum < 0:
            Total = l_sum + root.val
        #If both sum are greater than zero.
        else:
            Total = l_sum + r_sum + root.val
        self.M = max(self.M, Total)

        #Base on sum of left and right tree. Follow belowed answers.
        if l_sum < 0 and r_sum < 0:
            print ("KAM")
            return root.val
        elif l_sum < 0:
            return r_sum + root.val
        elif r_sum < 0:
            return l_sum + root.val
        else:
            return max(l_sum, r_sum) + root.val
    def maxPathSum(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.M

# my Answer 2
class Solution:
    def __init__(self):
        self.M = -sys.maxsize-1
    def dfs(self, root:TreeNode) -> int:
        if not root:
            return 0
         # ignore paths with negative sums, since we need to find the maximum sum we should
    # ignore any path which has an overall negative sum.
        l_sum = max(0, self.dfs(root.left))
        r_sum = max (0, self.dfs(root.right))

        # maximum path sum at the current node will be equal to the sum from the left subtree +
    # the sum from right subtree + val of current node
        Total = l_sum + r_sum + root.val
        self.M = max(self.M, Total)
         # maximum sum of any path from the current node will be equal to the maximum of
    # the sums from left or right subtrees plus the value of the current node
        return max(l_sum, r_sum) + root.val

    def maxPathSum(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.M

#answer
import math


class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class MaximumPathSum:

  def find_maximum_path_sum(self, root):
    self.globalMaximumSum = -math.inf
    self.find_maximum_path_sum_recursive(root)
    return self.globalMaximumSum

  def find_maximum_path_sum_recursive(self, currentNode):
    if currentNode is None:
      return 0

    maxPathSumFromLeft = self.find_maximum_path_sum_recursive(
      currentNode.left)
    maxPathSumFromRight = self.find_maximum_path_sum_recursive(
      currentNode.right)

    # ignore paths with negative sums, since we need to find the maximum sum we should
    # ignore any path which has an overall negative sum.
    maxPathSumFromLeft = max(maxPathSumFromLeft, 0)
    maxPathSumFromRight = max(maxPathSumFromRight, 0)

    # maximum path sum at the current node will be equal to the sum from the left subtree +
    # the sum from right subtree + val of current node
    localMaximumSum = maxPathSumFromLeft + maxPathSumFromRight + currentNode.val

    # update the global maximum sum
    self.globalMaximumSum = max(self.globalMaximumSum, localMaximumSum)

    # maximum sum of any path from the current node will be equal to the maximum of
    # the sums from left or right subtrees plus the value of the current node
    return max(maxPathSumFromLeft, maxPathSumFromRight) + currentNode.val


def main():
  maximumPathSum = MaximumPathSum()
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)

  print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))
  root.left.left = TreeNode(1)
  root.left.right = TreeNode(3)
  root.right.left = TreeNode(5)
  root.right.right = TreeNode(6)
  root.right.left.left = TreeNode(7)
  root.right.left.right = TreeNode(8)
  root.right.right.left = TreeNode(9)
  print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))

  root = TreeNode(-1)
  root.left = TreeNode(-3)
  print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))


main()




'''
Time complexity
The time complexity of the above algorithm is O(N), where ‘N’ is the total number of nodes in the tree.
This is due to the fact that we traverse each node once.
Space complexity
The space complexity of the above algorithm will be O(N) in the worst case.
This space will be used to store the recursion stack.
The worst case will happen when the given tree is a linked list (i.e., every node has only one child).
'''
