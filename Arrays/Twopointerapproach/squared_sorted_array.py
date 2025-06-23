class Solution:
    def sortedSquares(self, nums):
        upd_arr = []
        left = None
        right = None
        
        if nums[0] >= 0:
            left = -1
            right = 0
        elif nums[0] < 0 and nums[len(nums)-1] < 0:
            left = len(nums) - 1
            right = len(nums)
        else:
            for i in range(1, len(nums)):
                if nums[i] >= 0 and nums[i - 1] < 0:
                    left = i - 1
                    right = i
                    break
        
        while (left >= 0 and right <= len(nums) - 1):
            left_value = nums[left]*nums[left]
            right_value = nums[right]*nums[right]
            if left_value < right_value:
                upd_arr.append(left_value)
                left = left - 1
            else:
                upd_arr.append(right_value)
                right = right + 1
        
        while left >= 0:
            left_value = nums[left]*nums[left]
            upd_arr.append(left_value)
            left = left - 1
        
        while right <= len(nums)-1:
            right_value = nums[right]*nums[right]
            upd_arr.append(right_value)
            right = right + 1
            
        return upd_arr
            
            
solution = Solution()
print(solution.sortedSquares([-1, 1]))


'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.


Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].


Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
 
Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
'''