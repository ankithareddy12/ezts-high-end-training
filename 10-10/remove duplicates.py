#Program to print missing element and remove duplicates in an array
def xor_approach(n,arr):
    ans=0
    for i in range(1,n+1):
        ans=ans^i
        if i!=n:
            ans=ans^arr[i-1]
    return ans
arr=[1,2,3,4,5,6,7,8,9,9]
print(xor_approach(10,arr))
unique_arr = list(set(arr))
print(unique_arr)
