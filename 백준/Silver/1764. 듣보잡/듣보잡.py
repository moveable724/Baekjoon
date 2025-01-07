import sys
input = sys.stdin.readline

n,m= map(int,input().split())
set_nh, set_ns = set(), set()


for __ in range(n):
    set_nh.add(input())
for _ in range(m):
    set_ns.add(input())
    
lst = (set_ns & set_nh)
lst =  list(lst)
lst.sort()
print(len(lst))
for i in lst:
    print(i, end='')