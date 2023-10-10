def print_subarrays(arr):
    n = len(arr)
    sub=[]
    sub3=[]
    for i in range(n):
        for j in range(i, n):
            subarray = arr[i:j + 1]
            sub.append(subarray)

x = [1,2,3,4]
print_subarrays(x)

