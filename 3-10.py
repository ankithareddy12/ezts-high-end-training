"""
#subset sum
def is_subset_sum_possible(nums, target_sum):
    dp = [False] * (target_sum + 1)
    dp[0] = True
    
    for num in nums:
        for j in range(target_sum, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    
    return dp[target_sum]

# Example usage
nums = [3, 34, 4, 12, 5, 2]
target_sum = 9
result = is_subset_sum_possible(nums, target_sum)
print(result)

#bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to optimize by avoiding unnecessary passes if the list is already sorted
        swapped = False

        for j in range(0, n-i-1):
            # Compare adjacent elements
            if arr[j] > arr[j+1]:
                # Swap them if they are in the wrong order
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        # If no two elements were swapped in the inner loop, the array is already sorted
        if not swapped:
            break

my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)
print("Sorted array is:", my_list)
def is_balanced_parentheses(s):
    stack = []  # Create an empty stack

    # Define a dictionary to map closing parentheses to their corresponding opening parentheses
    parentheses_map = {')': '(', '}': '{', ']': '['}


    for char in s:
        if char in '({[':
            
            stack.append(char)
        elif char in ')}]':
           
            if not stack:
                return False 
            top_element = stack.pop()
            if parentheses_map[char] != top_element:
                return False  
    return not stack


test_string = "{[()]}"  
result = is_balanced_parentheses(test_string)
if result:
    print(f"'{test_string}' has balanced parentheses.")
else:
    print(f"'{test_string}' does not have balanced parentheses.")

#balenced parenthesis:
stack=[]
s=input()
n=len(s)
c=0
flag=1
if s[0]==']' or s[0]=='}' or s[0]==')':
    print(False)
else:
    for i in range(n):
        if s[i]=='[' or s[i]=='(' or s[i]=='{':
            stack.append(s[i])
            c+=1
        elif s[i]==']' or s[i]=='}' or s[i]==')':
            if stack==[]:
                flag=0
                break
            if (stack[-1]=='{' and s[i]=='}') or (stack[-1]=='[' and s[i]==']') or (stack[-1]=='(' and s[i]==')'):
                stack.pop()
                c-=1
            else:
                flag=0
                break
        else:
            flag=-1
            break
if flag==0 or c!=0:
    print("False")
elif flag==-1:
    print("Invalid Paranthesis")
else:
    print("True")

#balenced 
def is_balanced_parentheses(string):
    stack = []
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']
    
    for char in string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return "Balanced"  
            opening_bracket = stack.pop()
            if opening_brackets.index(opening_bracket) != closing_brackets.index(char):
                return "Not Balanced"  
    
    return len(stack) == 0
s=input()
print(is_balanced_parentheses(s))

#gnerate parenthesis
def paren(res,n,open,close,str):
    if open==close and close==n:
        res.append(str)
        return
    if open<n:
        paren(res,n,open+1,close,str+'(')
        paren(res,n,open+1,close,str+'[')
        paren(res,n,open+1,close,str+'{')
    if close<open:
        paren(res,n,open,close+1,str+')')
        paren(res,n,open,close+1,str+']')
    
        paren(res,n,open,close+1,str+'}')

def gen_par(n):
    res=[]
    paren(res,n,0,0,"")
    return res
n=int(input())
x=gen_par(n)
for i in x:
    print(i)


#generate parenthesis
def paren(res,n,open,close,str):
    print("res:",res,"open:",open,'close:',close,str)
    if open==close and close==n:
        res.append(str)
        return
    if open<n:
        paren(res,n,open+1,close,str+'(')
    if close<open:
        paren(res,n,open,close+1,str+')')
def gen_par(n):
    res=[]
    paren(res,n,0,0,"")
    return res
n=int(input())
x=gen_par(n)
for i in x:
    print(i)
#balenced   
 b = input()
if len(b) % 2 == 0:
    n = len(b) - 1
    if b[0] == ']' or b[0] == '}' or b[0] == ')':
        print("Invalid Parenthesis")
    elif b[n] == '[' or b[n] == '{' or b[n] == '(':
        print("Invalid Parenthesis")
    else:
        ob = []
        cb = []
        for i in b:
            if i == '{' or i == '[' or i == '(':
                ob.append(i)
            else:
                cb.append(i)
        if len(ob) == len(cb):
            s = []
            for i in b:
                if i == '[' or i == '{' or i == '(':
                    s.append(i)
                elif i == ']' or i == '}' or i == ')':
                    if len(s) == 0:
                        print("Invalid Parenthesis")
                        break
                    if (i == ']' and s[-1] == '[') or (i == '}' and s[-1] == '{') or (i == ')' and s[-1] == '('):
                        s.pop()
                    else:
                        print("Invalid Parenthesis")
                        break
            else:
                if len(s) == 0:
                    print("Valid")
                else:
                    print("Invalid Parenthesis")
        else:
            print("Invalid Parenthesis")
else:
    print("Invalid Parenthesis")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    """


