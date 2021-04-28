'''
Problem Statement
Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.
Example 1:
Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]
Example 2:
Input: [-3, -1, 0, 1, 2]
Output: [0 1 1 4 9]
'''
# my code
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left, right = 0, length -1
        highestindex = length -1
        result = [0 for x in range(len(nums))]

        while left <= right:
            leftsqr = nums[left]* nums[left]
            rightsqr = nums[right]* nums[right]

            # If right element square is more than left square then add to new list and traverse by reducing 1 index less on right
            # else increase left index and traverse
            if leftsqr < rightsqr:
                result[highestindex] = rightsqr
                right -=1
            else:
                result[highestindex] = leftsqr
                left += 1
            highestindex -=1

        return result
        
#answer
def make_squares(arr):
  n = len(arr)
  squares = [0 for x in range(n)]
  highestSquareIdx = n - 1
  left, right = 0, n - 1
  while left <= right:
    leftSquare = arr[left] * arr[left]
    rightSquare = arr[right] * arr[right]
    if leftSquare > rightSquare:
      squares[highestSquareIdx] = leftSquare
      left += 1
    else:
      squares[highestSquareIdx] = rightSquare
      right -= 1
    highestSquareIdx -= 1

  return squares


def main():

  print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
  print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()


'''
Time complexity
The time complexity of the above algorithm will be O(N) as we are iterating the input array only once.
Space complexity
The space complexity of the above algorithm will also be O(N); this space will be used for the output array.
'''
