#implement a 2d array and rotate 90 degrees
"""def rotate_90(matrix):
    rows=len(matrix)
    cols=len(matrix(0))
    rotated_matrix=([0]*rows for i in range(cols))
    
    for i in range(rows):
        for j in range(cols):
            rotated_matrix[j][rows-1-i]=matrix[i][j]
    return rotated_matrix
original_matrix=[[1,2,3],
                 [4,5,6],
                 [7,8,9]]
rotated_matrix=rotate_90(original_matrix)
for row in rotated_matrix:
    print(rows)
def fun(x,a):
    for i in range(int(x/2)):
        for j in range(i,x-i-1):
            temp=a[i][j]
            a[i][j]=a[x-j-1][i]
            a[x-j-1][i]=a[x-i-1][x-j-1]
            a[x-i-1][x-j-1]=a[j][x-i-1]
            a[j][x-i-1]=temp
    return a
            
x=int(input())
a=[]
for i in range(x):
    c=list(map(int,input().split()))
    a.append(c)
r=fun(x,a)
print(r)
for i in r:
    print(" ".join(map(str,i)))

list=list(range(10,31))
print(list)
for i in range(10,31):
    if i%2==0 and 2^i:
        print(i)"""

l,u=int(input()),int(input())
size=int(input("Enter array size:"))
print("Enter Array elements:")
ele=[]
for i in range(size):
    e=int(input())
    if l<=e<=u:
        ele.append(e)
    else:
        print("Enter between",l,"and",u)
e=[]
res=[]
for i in ele:
    if i%2==0:
        e.append(i)
    if i&(i-1) ==0:
        res.append(i)
    else:
        continue
print(e)
print(res)    







