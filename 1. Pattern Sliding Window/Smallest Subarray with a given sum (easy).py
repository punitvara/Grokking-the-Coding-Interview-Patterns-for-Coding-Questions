'''
Problem Statement
Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.
Example 1:
Input: [2, 1, 5, 2, 3, 2], S=7
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].
Example 2:
Input: [2, 1, 5, 2, 8], S=7
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
Example 3:
Input: [3, 4, 1, 1, 6], S=8
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].
'''

#mycode
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_win = math.inf
        win_sum  = 0
        win_start = 0

        for win_end in range(len(nums)):
            win_sum += nums[win_end]

            while win_sum >=target:
                min_win = min(min_win, win_end - win_start +1)
                print (min_win)
                win_sum = win_sum - nums[win_start]
                win_start = win_start + 1
        if (min_win == math.inf):
            return 0
        return min_win

#Answer
import math

def smallest_subarray_with_given_sum(s, arr):
  window_sum = 0
  min_length = math.inf
  window_start = 0

  for window_end in range(0, len(arr)):
    window_sum += arr[window_end]  # add the next element
    # shrink the window as small as possible until the 'window_sum' is smaller than 's'
    while window_sum >= s:
      min_length = min(min_length, window_end - window_start + 1)
      window_sum -= arr[window_start]
      window_start += 1
  if min_length == math.inf:
    return 0
  return min_length

  '''
Time Complexity
The time complexity of the above algorithm will be O(N).
The outer for loop runs for all elements and the inner while loop processes each element only once, therefore the time complexity of the algorithm will be O(N+N) which is asymptotically equivalent to O(N).
Space Complexity
The algorithm runs in constant space O(1).
'''
