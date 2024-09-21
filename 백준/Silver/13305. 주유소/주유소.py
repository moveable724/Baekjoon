import sys
input = sys.stdin.readline
n= int(input())
road= list(map(int, input().split()))
price= list(map(int, input().split()))
min_idx=0
tot_sum=0
while True:
    i=min_idx
    if i >= n-1:
        break
    if i == price.index(min(price[i:])):
        tot_sum+=price[i]*sum(road[i:])
        break
    for x in range(i,n):
        if price[x]<price[i]:
            min_idx=x
            break
    
    tot_sum+=price[i]*sum(road[i:min_idx])
    
print(tot_sum)