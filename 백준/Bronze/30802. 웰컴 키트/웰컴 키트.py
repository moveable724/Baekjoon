import sys
input = sys.stdin.readline
n=int(input())
lst = list(map(int, input().split()))
t,p = map(int, input().split())
for i in range(len(lst)):
    if lst[i] % t==0:
        lst[i] = lst[i] // t
    else: lst[i] = lst[i]// t +1
        
print(sum(lst))
print(n//p, n%p)