'''
Problem Statement
Given a set of positive numbers, determine if a subset exists whose sum is equal to a given number ‘S’.
Example 1:
Input: {1, 2, 3, 7}, S=6
Output: True
The given set has a subset whose sum is '6': {1, 2, 3}
Example 2:
Input: {1, 2, 7, 1, 5}, S=10
Output: True
The given set has a subset whose sum is '10': {1, 2, 7}
Example 3:
Input: {1, 3, 4, 8}, S=6
Output: False
The given set does not have any subset whose sum is equal to '6'.
'''


#Recursive Solution

class Solution:
    def isSubsetSum (self, N, arr, sum):
        # code here
        if (N == 0 and sum == 0):
            return 1
        if (N == 0 and sum != 0):
            return 0
        if arr[N-1] <= sum:
            return self.isSubsetSum(N-1, arr, sum-arr[N-1]) or self.isSubsetSum(N-1, arr, sum)
        elif arr[N-1] > sum:
            return self.isSubsetSum(N-1, arr, sum)
