def two_sum(nums, target):
    nums.sort()
    left, right = 0, len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [nums[left], nums[right]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return None  

nums = [2,3,5,7,10,12,15,21]
target = 19
result = two_sum(nums, target)
print(result)  