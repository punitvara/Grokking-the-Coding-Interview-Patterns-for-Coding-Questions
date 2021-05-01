'''
Triplet Sum Close to Target (medium)
Problem Statement
Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet.
If there are more than one such triplet, return the sum of the triplet with the smallest sum.
Example 1:
Input: [-2, 0, 1, 2], target=2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.
Example 2:
Input: [-3, -1, 1, 2], target=1
Output: 0
Explanation: The triplet [-3, 1, 2] has the closest sum to the target.
Example 3:
Input: [1, 0, 1, 1], target=100
Output: 3
Explanation: The triplet [1, 1, 1] has the closest sum to the target.
'''

# my answer
'''
Aim of this problem is to reduce distance between sum and target. return element wherever you find difference is min. If we want to find minimum diff, ultimetely it means we want to find max sum.
take example [-1 2 1 -4] and target = 1

possible combinations of triplets:
-1 2  1 sum = 2  difference = target - sum = 1 - 2 = -1
-1 1 -4 sum = -4 difference = 1 - (-4) = 5
 2 1 -4 sum = -1 difference = 1 - (-1) = 2

In above solution minimum diff we see is -1. Here is difference can be seen as distance between two so sign doesnt matter. consider absolute of diff and see which one is minimum. Wherever diff is minimum, sum will be the biggest. Hence return sum where diff is minimum.

There two possibility of tracking:-
1. biggest sum
2. smallest diff between target and sum.

First one is easier for understanding and coding.

'''

import sys
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        # variable to track biggest sum.
        closet_sum = -sys.maxsize -1

        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) -1
            while (left < right):
                # triplet sum
                triplet_sum = nums[left] + nums[i] + nums[right]
                if target - triplet_sum == 0:
                    return triplet_sum
                #if current difference between target and triplet sum is less than  minimum diff of target - privous closest triplet_sum, then current triplet sum is closest sum because when diff is minimum, triplet sum will be maximum
                if abs(target - triplet_sum) < abs(target - closet_sum):
                    closet_sum = triplet_sum
                # if triplet sum is more than target then we need smaller sum then target
                if triplet_sum > target:
                    right -= 1
                else:
                    left += 1 #if triplet sum is less than target then we need bigger sum then target
        return closet_sum

#answer
import math
def triplet_sum_close_to_target(arr, target_sum):
  arr.sort()
  smallest_difference = math.inf
  for i in range(len(arr)-2):
    left = i + 1
    right = len(arr) - 1
    while (left < right):
      target_diff = target_sum - arr[i] - arr[left] - arr[right]
      if target_diff == 0:  # we've found a triplet with an exact sum
        return target_sum - target_diff  # return sum of all the numbers

      # the second part of the following 'if' is to handle the smallest sum when we have more than one solution
      if abs(target_diff) < abs(smallest_difference) or (abs(target_diff) == abs(smallest_difference) and target_diff > smallest_difference):
        smallest_difference = target_diff  # save the closest and the biggest difference

      if target_diff > 0:
        left += 1  # we need a triplet with a bigger sum
      else:
        right -= 1  # we need a triplet with a smaller sum

  return target_sum - smallest_difference


def main():
  print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
  print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
  print(triplet_sum_close_to_target([1, 0, 1, 1], 100))


main()


'''
Time complexity
Sorting the array will take O(N* logN)O(N∗logN). Overall searchTriplet() will take O(N * logN + N^2),
which is asymptotically equivalent to O(N^2).
Space complexity
The space complexity of the above algorithm will be O(N) which is required for sorting.
'''
