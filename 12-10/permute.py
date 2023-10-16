def permute(arr):
    if len(arr)==1:
        return [arr]
    ans=[]
    for i in range(len(arr)):
        x=[arr[i]]
        n_arr=arr[:i]+arr[i+1:]
        for i in permute(n_arr):
            ans.append(x+i)
    return ans
print(permute([1,2,3]))