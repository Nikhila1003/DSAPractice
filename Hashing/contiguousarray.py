from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sumval = 0
        summap = {0:-1}
        result = 0
        
        for index, value in enumerate(nums):
            if value == 0:
                sumval += -1
            else:
                sumval += 1
            
            if sumval in summap:
                new_result = index - summap[sumval]
                if new_result > result:
                    result = new_result
            else:
                summap[sumval] = index
        
        return result

sol = Solution()
print(sol.findMaxLength([0,1,1,1,1,1,0,0,0]))

'''
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
'''