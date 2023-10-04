"""for i in range(1,11):
    print(i)
int x=967070125768125125301
#inheritance
class A:
    x=10
    __y=20
    def s(self):
        print("add")
    def work(self,x):
        self.x=x
        print(x)
class B(A):
    print("i")
    

obj=B()
print(obj.x)

#class consists of three variables one string 2 integers and create one method
#and find reverse of string and squareroot then other method find length of string
#modulus of integers
class A:
    def m1(self,x,y):
        self.x=x
        print(x[::-1])
        self.y=y
        print(y*2)
    def displayresults(self,x,a,b):
        print(len(x))
        print(a%b)
obj=A()
obj.m1("Hello",20)
obj.displayresults("Hello",20,20)

#class consists of three variables one string 2 integers and create one method
#and find reverse of string and squareroot then other method find length of string
#modulus of integers
class A:
    def __init__(self):
        self.a = input("Enter the string:")
        self.b = int(input("Enter the number:"))
        self.c = int(input("Enter the number:"))
        
    def m1(self):
        print(self.a[::-1])
        print(self.b**2)
        
    def DisplayResults(self):
        print(len(self.a))
        print(self.b % self.c)

obj = A()

obj.m1()
obj.DisplayResults()


class A:
    a=10
    def m1(self,a):
        print(a)
        a=self.a
    def m2(self):
        print(self.a)
obj=A()
obj.m1(20)
obj.m2()

#stack
l=[]
l.append(10)
l.append(20)
l.append(30)
l.append(40)
print(l)
print(l[-1])
print(l.pop())
print(l.pop())

#from list
l=[]
n=int(input())
for i in range(n):
    l.append(int(input()))
print(l)
for i in range(n):
    print(l.pop())"""
    

#from dequeue
from collections import deque
l=deque()
n=int(input())
for i in range(n):
    l.append(int(input()))
print(l)
for i in range(n):
    print(l.popleft())
print(l)















