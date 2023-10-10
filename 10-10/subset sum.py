def is_subset_sum_possible(nums, target_sum):
    dp = [False] * (target_sum + 1)
    dp[0] = True
    
    for num in nums:
        for j in range(target_sum, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    
    return dp[target_sum]

# Example usage
nums = [3, 34, 4, 12, 5, 2]
target_sum = 3
result = is_subset_sum_possible(nums, target_sum)
print(result)