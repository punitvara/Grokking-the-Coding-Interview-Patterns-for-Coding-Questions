'''
Rotate Array
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
'''

# Extra memory Solution
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Extra memory solution
        if nums is None:
            return nums
        length = len(nums)

        if k > length:
            k = k % length

        if  k == 0 or length == k:
            return nums
        # create a new array of same length as originial
        result = [0] * length

        # Add values to new array from original array
        for i in range(length):
            # remember indexing to rotate array
            result[(i+k) % length] = nums[i]

        nums[:] = result
