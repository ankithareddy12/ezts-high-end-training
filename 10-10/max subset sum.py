def max_subarray_sum(arr):
    if not arr:
        return None

    max_sum = arr[0]
    current_sum = arr[0]
    start = end = 0
    current_start = 0
    c=0

    for i in range(1, len(arr)):
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            current_start = i
            c+=1
        else:
            current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = current_start
            end = i
            c+=1

    return arr[start:end + 1]
    print(c)

# Example usage
input_array = [-3,-2,-19,18,6,-3,15,9,-17,2]
result = max_subarray_sum(input_array)
print("Subarray with Highest Sum:", result)
