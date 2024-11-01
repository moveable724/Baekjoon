n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n   
prev = [-1] * n      

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            prev[i] = j  

lis_length = max(dp)
idx = dp.index(lis_length)

lis_sequence = []
while idx != -1:
    lis_sequence.append(arr[idx])
    idx = prev[idx]
lis_sequence.reverse()  

# 결과 출력
print(lis_length)
print(*lis_sequence)
