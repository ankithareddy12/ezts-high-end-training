"""# Take input from the user in the format "name and code"
user_input = input("Enter name and code (separated by a space): ")

# Split the input into name and code
name, code = user_input.split()

# Initialize variables to store the maximum digit and final string
max_digit = -1
final_string = ""

# Iterate through the characters in the code
for char in code:
    if char.isdigit():
        digit = int(char)
        if digit <= len(name):
            max_digit = max(max_digit, digit)

# Construct the final string
if max_digit != -1:
    final_string = name[:max_digit] + code + name[max_digit:]
else:
    final_string = name + ":x"

print("Final String:", final_string)"""
s=input()
los=s.split(',')
op=''
for i in los:
    nc=i.split(':')
    name=nc[0]
    code=nc[1]
    l=len(name)
    max=0
    for i in code:
        if int(i)>max and int(i)<=len(name):
            max=int(i)
    if max==0:
        op+='X'
    else:
        op+=name[max-1]
print(op
