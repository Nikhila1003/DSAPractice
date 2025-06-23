class Solution:
    def minStartValue(self, nums):
        prefix_sum = nums[0]
        min_prefix = nums[0]

        for idx in range(1, len(nums)):
            prefix_sum += nums[idx]
            if prefix_sum < min_prefix:
                min_prefix = prefix_sum 
        
        if min_prefix < 0:
            return abs(min_prefix - 1)
        else:
            return 1

solution = Solution()
print(solution.minStartValue([-3,2,-3,4,2]))


'''
Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.

Example 1:

Input: nums = [-3,2,-3,4,2]
Output: 5
Explanation: If you choose startValue = 4, in the third iteration your step by step sum is less than 1.
step by step sum
startValue = 4 | startValue = 5 | nums
  (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
  (1 +2 ) = 3  | (2 +2 ) = 4    |   2
  (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
  (0 +4 ) = 4  | (1 +4 ) = 5    |   4
  (4 +2 ) = 6  | (5 +2 ) = 7    |   2
'''