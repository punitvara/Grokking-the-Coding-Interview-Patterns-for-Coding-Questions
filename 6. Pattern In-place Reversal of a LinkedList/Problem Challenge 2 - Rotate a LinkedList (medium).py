'''
Problem Challenge 2
Rotate a LinkedList (medium)
Given the head of a Singly LinkedList and a number ‘k’, rotate the LinkedList to the right by ‘k’ nodes.
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return head

        curr = head
        # Save length of linkedlist
        length = 0

        # Get length of linkedlist
        while curr is not None:
            last = curr
            curr = curr.next
            length += 1

        # Tricky corner case. if K is more than length then figure out effective k.
        if k > length:
            k = k % length

        # corner case 2. If K= 0 and length, then return LL as it is.
        if k == 0 or k == length:
            return head

        # Nodes to traverse
        traverse = length - k

        # Change curr again to head because we traversed it earlier.
        curr = head
        while curr is not None and traverse > 0:
            prev = curr
            curr = curr.next
            traverse = traverse - 1

        # Traverse k nodes and link last node to None
        prev.next = None

        # Link last node to head of linkedlist
        last.next = head

        # Change head to curr node after traversal
        head = curr

        return head

#answer
from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()


def rotate(head, rotations):
  if head is None or head.next is None or rotations <= 0:
    return head

  # find the length and the last node of the list
  last_node = head
  list_length = 1
  while last_node.next is not None:
    last_node = last_node.next
    list_length += 1

  last_node.next = head  # connect the last node with the head to make it a circular list
  rotations %= list_length  # no need to do rotations more than the length of the list
  skip_length = list_length - rotations
  last_node_of_rotated_list = head
  for i in range(skip_length - 1):
    last_node_of_rotated_list = last_node_of_rotated_list.next

  # 'last_node_of_rotated_list.next' is pointing to the sub-list of 'k' ending nodes
  head = last_node_of_rotated_list.next
  last_node_of_rotated_list.next = None
  return head


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = rotate(head, 3)
  print("Nodes of rotated LinkedList are: ", end='')
  result.print_list()


main()



'''
Time complexity
The time complexity of our algorithm will be O(N) where ‘N’ is the total number of nodes in the LinkedList.
Space complexity
We only used constant space, therefore, the space complexity of our algorithm is O(1).
'''
