'''
Problem Statement
We are given an unsorted array containing numbers taken from the range 1 to ‘n’.
The array can have duplicates, which means some numbers will be missing. Find all those missing numbers.
Example 1:
Input: [2, 3, 1, 8, 2, 3, 5, 1]
Output: 4, 6, 7
Explanation: The array should have all numbers from 1 to 8, due to duplicates 4, 6, and 7 are missing.
Example 2:
Input: [2, 4, 1, 2]
Output: 3
Example 3:
Input: [2, 3, 2, 1]
Output: 4
'''

# my code
'''
If we sort array/list with cyclic sort then all elements will be placed in respective index and duplicates elements will stay at missing number index.

For example
x = [3,2,2,1] result would be [1,2,3,2]
x = [4,3,2,7,8,2,3,1] result would be [1, 2, 3, 4, 3, 2, 7, 8]
'''
#my code (cyclic sort)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        length = len(nums)
        final_list = []

        while i < length:
            j = nums[i] - 1 # check current array element -1 should be equal to index
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i = i+ 1
        #check for missing number in array, since index start from 1 save i+1 in final list
        for i in range(length):
            if nums[i] != i +1:
                final_list.append(i+1)
        return final_list

#someones else code without cyclic sort 
def find_missing_numbers(nums):
  missingNumbers = []
  # TODO: Write your code here
  for i in range(len(nums)):
    j=abs(nums[i])-1
    if nums[j] >= 0:
      nums[j] = -nums[j]

  for i in range(len(nums)):
    if nums[i] > 0:
      missingNumbers.append(i+1)
  return missingNumbers

#answer
def find_missing_numbers(nums):
  i = 0
  while i < len(nums):
    j = nums[i] - 1
    if nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]  # swap
    else:
      i += 1

  missingNumbers = []

  for i in range(len(nums)):
    if nums[i] != i + 1:
      missingNumbers.append(i + 1)

  return missingNumbers


def main():
  print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
  print(find_missing_numbers([2, 4, 1, 2]))
  print(find_missing_numbers([2, 3, 2, 1]))


main()


'''
Time complexity
The time complexity of the above algorithm is O(n).
Space complexity
Ignoring the space required for the output array, the algorithm runs in constant space O(1).
'''
