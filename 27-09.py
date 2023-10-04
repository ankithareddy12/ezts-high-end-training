"""p=100000
r=0.12/12
t=4
si=(p*r*t)
print(si)
month=int(input())
for month in range(1,13):
    if month==5:
        p-=25000
        si=p*t*r
        print(si)
        t=int(input())
        for month in range(1,13):
            if month==9:
                p+=10000
                si=p*r*4
                print(si)
sum=si+si+si+p
print(sum)
    
a=100
print(id(a))
a=200
print(id(a))

for i in range(0,5):
    print(i)
print(i)

#sum of digits of given number
sum=0
n=int(input())
while(n!=0):
    sum=sum+(n%10)
    n=n//10
print(sum)

n=int(input())
sum=0
for i in str(n):
    sum=sum+int(i)
print(sum)"""
    
n=int(input())
temp=n
sum=0
for i in range(1,n,n//10):
    rem=sum+int(temp%10)
    temp=temp//10
print(sum)


























