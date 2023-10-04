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

'''Implement a 2d array and take to the matrix 90 deg'''
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
    print(" ".join(map(str,i))
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

