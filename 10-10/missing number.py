#Program to print missing element in an array
def xor_approach(n,arr):
    ans=0
    for i in range(1,n+1):
        ans=ans^i
        if i!=n:
            ans=ans^arr[i-1]
    return ans
print(xor_approach(10,[3,4,1,2,9,9,6,5,8,10]))
