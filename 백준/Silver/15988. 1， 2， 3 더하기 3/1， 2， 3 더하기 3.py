dp=[0]*1000001
import sys
input=sys.stdin.readline

dp[0]=1
dp[1]=1
dp[2]=2
for i in range(3,len(dp)):
    dp[i]=(dp[i-1]+dp[i-2]+dp[i-3])%1000000009

n=int(input())
for i in range(n):
    print(dp[int(input())])