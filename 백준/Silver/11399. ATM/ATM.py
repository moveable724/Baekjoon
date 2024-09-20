n=int(input())
lst=sorted(list(map(int,input().split())))
dp=lst[:]
for i in range(1,len(dp)):
    dp[i] = dp[i-1]+dp[i]
print(sum(dp))