import sys
input = sys.stdin.readline
n, m = map(int, input().split())
lst= list(map(int, input().split()))
sum_list = [0]*n
sum_list[0] = lst[0]

for i in range(1,n):
    sum_list[i] = sum_list[i-1] + lst[i]
target_list = []
for i in range(m):
    target_list.append(list(map(int, input().split())))
for i in target_list:
    if i[0] < 2:
        print(sum_list[i[1]-1])
    else:
        print(sum_list[i[1]-1] - sum_list[i[0]-2])
