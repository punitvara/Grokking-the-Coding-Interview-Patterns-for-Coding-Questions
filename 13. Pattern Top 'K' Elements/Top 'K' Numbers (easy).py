'''
Problem Statement
Given an unsorted array of numbers, find the âKâ largest numbers in it.
Note: For a detailed discussion about different approaches to solve this problem, take a look at Kth Smallest Number.
Example 1:
Input: [3, 1, 5, 12, 2, 11], K = 3
Output: [5, 12, 11]
Example 2:
Input: [5, 12, 11, -1, 12], K = 3
Output: [12, 11, 12]
'''

# my code 1 (code to find kth largest number) solved on leetcode
from heapq import *

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # put first 'K' numbers in the min heap
        min_heap = []

        for i in range(k):
            heappush(min_heap, nums[i])

        # Go through remaining numbers in array. if the number from array is bigger than the
        # top (smallest) number of min-heap, remove top number from heap and add the number from array.
        for i in range(k, len(nums)):
            if nums[i] > min_heap[0]:
                heappop(min_heap)
                heappush(min_heap, nums[i])

        #First element of list would be largest
        return min_heap[0]

# my code 2 (Try to solve problem this way. More generalized way to solve problems)
# Solved using another technique other than used in goraking interview solutions
# This could be easy to remember and use.

from heapq import *

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # put first 'K' numbers in the min heap
        min_heap = []

        for i in range(len(nums)):

            if len(min_heap) ==k:
                heappush(min_heap, nums[i])
                heappop(min_heap)
            else:
                heappush(min_heap, nums[i])

        return min_heap[0]

#answer
from heapq import *


def find_k_largest_numbers(nums, k):
  minHeap = []
  # put first 'K' numbers in the min heap
  for i in range(k):
    heappush(minHeap, nums[i])

  # go through the remaining numbers of the array, if the number from the array is bigger than the
  # top(smallest) number of the min-heap, remove the top number from heap and add the number from array
  for i in range(k, len(nums)):
    if nums[i] > minHeap[0]:
      heappop(minHeap)
      heappush(minHeap, nums[i])

  # the heap has the top 'K' numbers, return them in a list
  return list(minHeap)


def main():

  print("Here are the top K numbers: " +
        str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

  print("Here are the top K numbers: " +
        str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))


main()



'''
Time complexity
As discussed above, the time complexity of this algorithm is O(K*logK+(N-K)*logK), which is asymptotically equal to O(N*logK)
Space complexity
The space complexity will be O(K) since we need to store the top âKâ numbers in the heap.
'''
