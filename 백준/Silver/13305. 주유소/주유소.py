import sys
input = sys.stdin.readline

n = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

tot_sum = 0
current_price = price[0]

for i in range(n - 1):
    if price[i] < current_price:
        current_price = price[i]
    tot_sum += current_price * road[i]

print(tot_sum)