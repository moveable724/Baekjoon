import sys
input = sys.stdin.readline
dp=[0]*101
dp[:6] = [0,1,1,1,2,2]

for i in range(6,101):
    dp[i] = dp[i-1]+dp[i-5]

n = int(input())


for i in range(n):
    num=int(input())
    print(dp[num])