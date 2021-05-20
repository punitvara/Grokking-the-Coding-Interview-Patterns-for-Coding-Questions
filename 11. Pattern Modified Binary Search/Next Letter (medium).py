'''
Problem Statement
Given an array of lowercase letters sorted in ascending order,
find the smallest letter in the given array greater than a given ‘key’.
Assume the given array is a circular list, which means that the last letter is assumed to be connected with the first letter.
This also means that the smallest letter in the given array is greater than the last letter of the array and is also the first letter of the array.
Write a function to return the next letter of the given ‘key’.
Example 1:
Input: ['a', 'c', 'f', 'h'], key = 'f'
Output: 'h'
Explanation: The smallest letter greater than 'f' is 'h' in the given array.
Example 2:
Input: ['a', 'c', 'f', 'h'], key = 'b'
Output: 'c'
Explanation: The smallest letter greater than 'b' is 'c'.
Example 3:
Input: ['a', 'c', 'f', 'h'], key = 'm'
Output: 'a'
Explanation: As the array is assumed to be circular, the smallest letter greater than 'm' is 'a'.
Example 4:
Input: ['a', 'c', 'f', 'h'], key = 'h'
Output: 'a'
Explanation: As the array is assumed to be circular, the smallest letter greater than 'h' is 'a'.
'''

# my code(see answer for even better solution)
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start = 0
        end = len(letters) -1
        if target == letters[len(letters) - 1]:
            return letters[0]
        while start <= end:
            mid = start + (end - start) //2

            if letters[mid] == target:
                if letters[mid] == letters[mid + 1]:
                    i = mid
                    while i < len(letters):
                        if (letters[mid] != letters[i]):
                            return letters[i]
                        i = i + 1
                    if i == len(letters):
                        return letters[0]
                else:
                    return letters[mid+1]
            elif letters[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        # very tricky to remember. When any char is greater than any of the element in array, your index will be pointing at len of array + 1. return 1st element bcz array is circular
        if start == len(letters):
            return letters[0]
        return letters[start]

#answer
def search_next_letter(letters, key):
  n = len(letters)
  if key < letters[0] or key > letters[n - 1]:
    return letters[0]

  start, end = 0, n - 1
  while start <= end:
    mid = start + (end - start) // 2
    if key < letters[mid]:
      end = mid - 1
    else: # key >= letters[mid]:
      start = mid + 1

  # since the loop is running until 'start <= end', so at the end of the while loop, 'start == end+1'
  return letters[start % n]


def main():
  print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))


main()



'''
Time complexity
Since, we are reducing the search range by half at every step,
this means that the time complexity of our algorithm will be O(logN)O
where ‘N’ is the total elements in the given array.
Space complexity
The algorithm runs in constant space O(1).
'''
