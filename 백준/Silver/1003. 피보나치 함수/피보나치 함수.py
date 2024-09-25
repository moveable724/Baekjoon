import sys
input = sys.stdin.readline

dp=[0]*41
dp[:3] = [0,1,1]
for i in range(2,len(dp)):
    dp[i] = dp[i-1]+dp[i-2]
    
    
n=int(input())
for i in range(n):
    num=int(input())
    if num == 0:
        print(1,0)
    else: print(dp[num-1],dp[num])

