import sys
input=sys.stdin.readline
n=int(input())
lst=[-10000]+list(map(int,input().split()))
dp=lst[:]
for i in range(1,len(dp)):
    dp[i] = max(lst[i], dp[i-1]+lst[i])
        
print(max(dp))