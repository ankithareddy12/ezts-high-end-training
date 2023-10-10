n=7564168
num=str(n)
s=''
for i in range(1,len(num),2):
    digit=int(num[i])
    print(digit)
    s+=str(int(digit)**2)
print(s,end=" ")
print(s[0:4])
    
    