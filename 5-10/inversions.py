def count_inversions_bruteforce(arr):
    n = len(arr)
    inversions = 0
    
    for i in range(n-1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inversions += 1
    
    return inversions

arr = [1,2,3,4]
inversions = count_inversions_bruteforce(arr)
print("Number of inversions:", inversions)