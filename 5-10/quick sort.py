def quicksort(arr):
    def sort(arr):
        if len(arr)<=1:
            return arr

        pivot=arr[len(arr)//2]
        left,middle,right = [], [], []
        for i in arr:
            (left if i<pivot else right if i> pivot else middle).append(i)
        return sort(left) + middle + sort(right)

    return sort(list(arr))
arr=list(map(int,input().split(",")))
sorted_array = quicksort(arr)
print("Sorted array:", sorted_array)
