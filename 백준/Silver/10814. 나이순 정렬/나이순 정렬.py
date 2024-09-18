import sys
input=sys.stdin.readline
n=int(input())
lst = []
for __ in range(n):
    lst.append(list(input().split()))
lst.sort(key=lambda x: int(x[0]))
for i in lst:
    print(' '.join(i))