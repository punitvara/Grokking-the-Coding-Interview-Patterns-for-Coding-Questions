'''
Problem Statement
In a non-empty array of integers, every number appears twice except for one, find that single number.
Example 1:
Input: 1, 4, 2, 1, 3, 2, 3
Output: 4
Example 2:
Input: 7, 9, 7
Output: 9
'''
#mycode
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = nums[0]
        for i in range(1, len(nums)):
            x = x ^ nums[i]
        return x

'''
Time Complexity:
Time complexity of this solution is O(n) as we iterate through all numbers of the input once.
Space Complexity:
The algorithm runs in constant space O(1).
'''
