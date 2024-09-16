import sys
input = sys.stdin.readline
dp1= [0]*100001
dp2= [0]*100001
dp3= [0]*100001
dp1[:4] = [0, 1, 0, 1]
dp2[:4] = [0, 0, 1, 1]
dp3[:4] = [0, 0, 0, 1]

for i in range(4,len(dp1)):
    dp3[i] = (dp1[i-3] + dp2[i-3]) % 1000000009
    dp2[i] = (dp1[i-2] + dp3[i-2]) % 1000000009
    dp1[i] = (dp2[i-1] + dp3[i-1]) % 1000000009


n=int(input())
for i in range(n):
    num=int(input())
    print((dp1[num] + dp2[num] + dp3[num]) % 1000000009)