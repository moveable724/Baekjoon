import sys
input = sys.stdin.readline

m,n = map(int,input().split())
dic = dict()
for __ in range(m):
    a,b = map(str,input().split())
    dic[a] = b
    
for _ in range(n):
    n = input().strip()
    print(dic[n])