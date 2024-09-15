def sum1(n):
    if n == 1 or n==0:
        return 1
    if n <0:
        return 0
    return sum1(n-1) + sum1(n-2) +sum1(n-3)
n = int(input())
for i in range(n):
    print(sum1(int(input())))