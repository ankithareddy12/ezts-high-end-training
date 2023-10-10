#row sum

for row in arr:
    if sum(row) != 15:

        return False

 

row sum

#col sum
for i in range(len(arr)):

    temp = 0

    for j in range(len(arr))

        temp += arr[j][i]

    if temp != 15:

        return False

col sum

# digit sum
for i in range(len(arr)):

    for j in range(len(arr))

        if i == j:

            temp += arr[i][j]

if temp != 15:

    return False

 

 

diag1 sum











