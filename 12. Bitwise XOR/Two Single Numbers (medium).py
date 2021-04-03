
'''
Problem Statement
In a non-empty array of numbers, every number appears exactly twice except two numbers that appear only once. Find the two numbers that appear only once.
Example 1:
Input: [1, 4, 2, 1, 3, 5, 6, 2, 3, 5]
Output: [4, 6]
Example 2:
Input: [2, 1, 3, 2]
Output: [1, 3]
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xy = 0
        #Get final XOR representation of two numbers
        for i in range(len(nums)):
            xy ^= nums[i]
        right_most_bit = 1

        #Try to find right most digit of xy representation. That's where two unique number have different bit. Hence output bit is 1
        while (right_most_bit & xy) == 0:
            right_most_bit = right_most_bit << 1

        num1, num2 = 0,0
        for i in range(len(nums)):
            if (nums[i] & right_most_bit) == 0:
                num1 ^= nums[i]
            else:
                num2 ^= nums[i]
        return [num2, num1]


#answer
def find_single_numbers(nums):
    # get the XOR of the all the numbers
    n1xn2 = 0
    for num in nums:
        n1xn2 ^= num

    # get the rightmost bit that is '1'
    rightmost_set_bit = 1
    while (rightmost_set_bit & n1xn2) == 0:
        rightmost_set_bit = rightmost_set_bit << 1
    num1, num2 = 0, 0

    for num in nums:
        if (num & rightmost_set_bit) != 0:  # the bit is set
            num1 ^= num
        else:  # the bit is not set
            num2 ^= num

    return [num1, num2]


def main():
    print('Single numbers are:' +
          str(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])))
    print('Single numbers are:' + str(find_single_numbers([2, 1, 3, 2])))


main()



'''
Time Complexity
The time complexity of this solution is O(n) where ‘n’ is the number of elements in the input array.
Space Complexity
The algorithm runs in constant space O(1).
'''
