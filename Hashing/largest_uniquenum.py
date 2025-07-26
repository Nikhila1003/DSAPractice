from collections import defaultdict
from typing import List

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        numcount = defaultdict(int)
        for num in nums:
            numcount[num] += 1
        
        lar_unique_num = -1
        for key in numcount:
            if numcount[key] == 1:
                temp = key
                if key > lar_unique_num:
                    lar_unique_num = temp
        
        return lar_unique_num 
    
sol = Solution()
print(sol.largestUniqueNumber([5,7,3,9,4,9,8,3,1]))

'''
Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1.
'''