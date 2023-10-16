n=7
row=n
col=2*n-1
start,end=n-1,n-1
for i in range(row):
    for j in range(col):
        if i==0 and j==n-1:
            print("*",end="")
        elif j>=start and j<=end:
            print(" ",end="")
        else:
            print("*",end="")
    print()
    start-=1
    end+=1
