def nthFibonaciNumber(n):
    if n<=0:
        return -1
    if n == 1:
        return 0
    if n == 2:
        return 1

    return nthFibonaciNumber(n-1)+nthFibonaciNumber(n-2)

print(nthFibonaciNumber(10))


