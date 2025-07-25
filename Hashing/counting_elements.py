class Solution:
    def countElements(self, arr) -> int:
        arrset = set(arr)
        
        count = 0
        for val in arr:
            if val+1 in arrset:
                count = count + 1

        return count
                
sol = Solution()
print(sol.countElements([1,2,3]))

'''
Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr.
If there are duplicates in arr, count them separately.

Input: arr = [1,2,3]
Output: 2
Explanation: 1 and 2 are counted cause 2 and 3 are in arr.

Input: arr = [1,1,3,3,5,5,7,7]
Output: 0
Explanation: No numbers are counted, cause there is no 2, 4, 6, or 8 in arr.
'''