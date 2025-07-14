def find_numbers(nums):
    ans = []
    nums_set = set(nums)

    for num in nums_set:
        if (num + 1 not in nums_set) and (num - 1 not in nums_set):
            ans.append(num)
    
    return ans

print(find_numbers([1,0,8,5,4,6,8]))

'''
Given an integer array nums, find all the numbers x in nums that satisfy the following: x + 1 is not in nums, and x - 1 is not in nums.

If a valid number x appears multiple times, you only need to include it in the answer once.
'''