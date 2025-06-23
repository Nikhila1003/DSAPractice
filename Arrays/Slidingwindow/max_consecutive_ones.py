class Solution:
    def longestOnes(self, nums, k: int) -> int:
        left = curr = ans = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                curr += 1
                
            while curr > k:
                if nums[left] == 0:   
                    curr -= 1
                left += 1
            
            val = right - left + 1
            if val > ans:
                ans = val
            
        return ans
    
s = Solution()
print(s.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))

'''
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
'''