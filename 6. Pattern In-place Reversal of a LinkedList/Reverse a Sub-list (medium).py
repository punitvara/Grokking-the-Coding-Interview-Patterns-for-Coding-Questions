'''
Problem Statement
Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Input: head = [5], left = 1, right = 1
Output: [5]
'''

# my code 1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# If we want to reverse a sub LL then three nodes are very important
# 1. Node after which we start reversing linkedlist and it will connect to first node of sub reversed linkedlist
# 2. Node from which we start reversing linked list and it will become last node of sub reversed linkedlist
# 3. Last node of sub linkedlist from which we dont want to reverse linked list

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head

        # after skipping 'left-1' nodes, current will point to 'left'th node
        current, previous = head, None
        count = 1
        while current is not None and count < left :
            previous = current
            current = current.next
            count += 1

        # we are interested in three parts of the LinkedList, the part before index 'left',
        # the part between 'left' and 'right', and the part after index 'right'
        last_node_of_first_part = previous
        # after reversing the LinkedList 'current' will become the last node of the sub-list
        last_node_of_sub_list = current

        # reverse nodes between 'left' and 'right'

        while current is not None and count < right  + 1:
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt
            count += 1

        # connect with the first part
        if last_node_of_first_part is not None:
            # 'previous' is now the first node of the sub-list
            last_node_of_first_part.next = previous
            # this means p == 1 i.e., we are changing the first node (head) of the LinkedList
        else:
            head = previous

        # connect with the last part
        last_node_of_sub_list.next = current

        return head


# Answer
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


def reverse_sub_list(head, p, q):
  if p == q:
    return head

  # after skipping 'p-1' nodes, current will point to 'p'th node
  current, previous = head, None
  i = 0
  while current is not None and i < p - 1:
    previous = current
    current = current.next
    i += 1

  # we are interested in three parts of the LinkedList, the part before index 'p',
  # the part between 'p' and 'q', and the part after index 'q'
  last_node_of_first_part = previous
  # after reversing the LinkedList 'current' will become the last node of the sub-list
  last_node_of_sub_list = current
  next = None  # will be used to temporarily store the next node

  i = 0
  # reverse nodes between 'p' and 'q'
  print(previous.value, current.value)
  while current is not None and i < q - p + 1:
    next = current.next
    current.next = previous
    previous = current
    current = next
    i += 1

  # connect with the first part
  if last_node_of_first_part is not None:
    # 'previous' is now the first node of the sub-list
    last_node_of_first_part.next = previous
  # this means p == 1 i.e., we are changing the first node (head) of the LinkedList
  else:
    head = previous

  # connect with the last part
  last_node_of_sub_list.next = current
  return head


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_sub_list(head, 2, 4)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()


'''
Time complexity
The time complexity of our algorithm will be O(N) where ‘N’ is the total number of nodes in the LinkedList.
Space complexity
We only used constant space, therefore, the space complexity of our algorithm is O(1).
'''
