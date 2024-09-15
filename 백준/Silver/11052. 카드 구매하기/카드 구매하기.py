import sys
input=sys.stdin.readline

n=int(input())
dp=[0]*(n+1)
lst = [0]+ list(map(int,input().split()))
dp[0] = 0
dp[1] = lst[1]

for i in range(1,len(dp)):
    for x in range(1,i+1):
        dp[i] = max(dp[i], dp[i-x] + lst[x])

print(dp[n])