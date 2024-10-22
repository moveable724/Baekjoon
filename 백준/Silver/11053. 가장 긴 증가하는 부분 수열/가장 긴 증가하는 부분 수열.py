import sys
input = sys.stdin.readline

n=int(input())
lst = list(map(int,input().split()))
dp=[1]*(n+1)
for i in range(n):
    for x in range(i):
        if lst[i]>lst[x]:
            dp[i] = max(dp[i],dp[x]+1)
            
            
print(max(dp))