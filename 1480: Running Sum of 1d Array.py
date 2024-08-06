
# Link: https://leetcode.com/problems/running-sum-of-1d-array/description/
# Difficulty: Easy
# Tags: 
# Problem
'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

'''


# Solution
'''
Used the prefix algorithm.
'''

# Code
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = []
        sum_from_left = 0
        for num in nums:
            sum_from_left += num
            prefix.append(sum_from_left)
        return prefix
        