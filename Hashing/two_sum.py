class Solution:
    def twoSum(self, nums, target: int):
        dic = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in dic: # This operation is O(1)!
                return [i, dic[complement]]
            
            dic[num] = i
        
        return [-1, -1]
    
sol = Solution()
print(sol.twoSum([5, 2, 7, 10, 3, 9], 8))


'''
Example 1: 1. Two Sum

Given an array of integers nums and an integer target, return indices of two numbers such that they add up to target. 
You cannot use the same index twice.
'''