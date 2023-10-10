def counting_sort(arr):
    # Find the range of values in the input array
    min_val = min(arr)
    max_val = max(arr)
    
    count_arr = [0] * (len(arr))
    print(count_arr)
    for num in arr:
        count_arr[num - min_val] += 1
    
    sorted_arr = []
    for i, count in enumerate(count_arr):
        sorted_arr.extend([i + min_val] * count)
    
    return sorted_arr
input_array = [2,1,1,0,2,5,4,0,2,8,7,7,9,2,0,1,9]
sorted_array = counting_sort(input_array)
print(sorted_array)
