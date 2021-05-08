'''
Problem Challenge 2
Find the Smallest Missing Positive Number (medium)
Given an unsorted array containing numbers, find the smallest missing positive number in it.
Example 1:
Input: [-3, 1, 5, 4, 2]
Output: 3
Explanation: The smallest missing positive number is '3'
Example 2:
Input: [3, -2, 0, 1, 2]
Output: 4
Example 3:
Input: [3, 2, 5, 1]
Output: 4
'''

'''
1. Consider array element as index
2. we want to focus elements which are positive, ignore negative numbers and zero
'''
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        i = 0
        while i < length:
            j = nums[i] - 1
            # only swap when array element is positive, or element is less than length and index and elemets are not same.
            if nums[i] > 0 and nums[i] <= length and nums[j] != nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i = i+1
        print (nums)
        for i in range(length):
            if nums[i]  != i + 1:
                return i + 1
        return length + 1

#answer
def find_first_missing_positive(nums):
  i, n = 0, len(nums)
  while i < n:
    j = nums[i] - 1
    if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]  # swap
    else:
      i += 1

  for i in range(n):
    if nums[i] != i + 1:
      return i + 1

  return nums.length + 1


def main():
  print(find_first_missing_positive([-3, 1, 5, 4, 2]))
  print(find_first_missing_positive([3, -2, 0, 1, 2]))
  print(find_first_missing_positive([3, 2, 5, 1]))


main()


'''
Time complexity
The time complexity of the above algorithm is O(n).
Space complexity
The algorithm runs in constant space O(1).
'''
