def check_for_target(nums, target):
    start = 0
    end = len(nums) - 1

    while start < end:
        if nums[start] + nums[end] == target:
            return True
        
        elif nums[start] + nums[end] < target:
            start += 1
        else:
            end -= 1
    
    return False


print(check_for_target([1, 2, 4, 6, 8, 9, 14, 15], 25))