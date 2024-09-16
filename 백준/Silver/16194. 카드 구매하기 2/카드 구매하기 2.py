import sys
input = sys.stdin.readline
n=int(input())
lst=[0]+list(map(int,input().split()))
dp= lst[:]
for i in range(1,len(dp)):
    for x in range(1,i+1):
        dp[i] = min(dp[i], dp[i-x] + lst[x])
        
print(dp[n])