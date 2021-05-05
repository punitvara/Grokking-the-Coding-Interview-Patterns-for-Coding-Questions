'''
Problem Statement
We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’.
The array has only one duplicate but it can be repeated multiple times.
Find that duplicate number without using any extra space. You are, however, allowed to modify the input array.
Example 1:
Input: [1, 4, 4, 3, 2]
Output: 4
Example 2:
Input: [2, 1, 3, 3, 5, 4]
Output: 3
Example 3:
Input: [2, 4, 1, 4, 4]
Output: 4
'''
#mycode

def find_duplicate(nums):
  # TODO: Write your code here
  for i in range(len(nums)):
    j=abs(nums[i])-1
    if nums[j] > 0:
      nums[j] = -nums[j]
    else:
      return j+1
  return -1


#mycode2

def find_duplicate(nums):
  # TODO: Write your code here
  i=0
  while i < len(nums):
    j=nums[i]-1

    if nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]
    elif nums[i] == nums[j] and i!=j:
      return nums[i]
    else:
      i += 1

  return -1

#answer

def find_duplicate(nums):
  i = 0
  while i < len(nums):
    if nums[i] != i + 1:
      j = nums[i] - 1
      if nums[i] != nums[j]:
        nums[i], nums[j] = nums[j], nums[i]  # swap
      else:  # we have found the duplicate
        return nums[i]
    else:
      i += 1

  return -1


def main():
  print(find_duplicate([1, 4, 4, 3, 2]))
  print(find_duplicate([2, 1, 3, 3, 5, 4]))
  print(find_duplicate([2, 4, 1, 4, 4]))


main()


'''
Time complexity
The time complexity of the above algorithm is O(n).
Space complexity
The algorithm runs in constant space O(1) but modifies the input array.
'''
