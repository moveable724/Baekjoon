import sys
input = sys.stdin.readline
n=int(input())

dp=[0]*(n+1)
lst=[0]
for i in range(n):
    lst.append(int(input()))
dp[0]=lst[0]
dp[1]=lst[0]+lst[1]
for i in range(2,n+1):
    dp[i]=max(lst[i]+dp[i-2], dp[i-3]+lst[i-1]+lst[i])
    
print(dp[n])