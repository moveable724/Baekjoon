import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

dp = [[0] * 2 for _ in range(n)]

dp[0][0] = lst[0]
dp[0][1] = -10000 
result = dp[0][0]

for i in range(1, n):
    dp[i][0] = max(lst[i], dp[i-1][0] + lst[i])
    
    dp[i][1] = max(dp[i-1][0], dp[i-1][1] + lst[i])
    
    result = max(result, dp[i][0], dp[i][1])

print(result)