'''
Problem Statement #
Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.
Example 1:
Input: [2, 1, 5, 1, 3, 2], k=3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:
Input: [2, 3, 4, 1, 5], k=2
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
'''
class Solution:
    def maximumSumSubarray (self,k,nums, N):
        max_sum = 0
        if k > len(nums):
            return sum(nums)
        if len(nums) == k:
            return sum(nums)
        temp_sum = 0

        for i in range(k):
            temp_sum += nums[i]
            max_sum = max(max_sum, temp_sum)

        if len(nums) -1 >= k:
            for i in range(k,len(nums)):
                temp_sum = temp_sum - nums[i-k] + nums[i]
                max_sum = max(max_sum, temp_sum)

        return max_sum

'''
Time Complexity
The time complexity of the above algorithm will be O(N).
Space Complexity
The algorithm runs in constant space O(1).
'''
