from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        ans = curr = 0

        for num in nums:
            curr += num
            ans += counts[curr - k]
            counts[curr] += 1
    
        return ans
    
sol = Solution()
print(sol.subarraySum([1, 2, 1, 2, 1], k = 3))

'''
Given an integer array nums and an integer k, find the number of subarrays whose sum is equal to k.
'''