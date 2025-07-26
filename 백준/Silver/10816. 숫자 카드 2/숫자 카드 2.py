import sys
input = sys.stdin.readline
n=int(input())
cards = sorted(list(map(int,input().split())), reverse='true')
m=int(input())
count_card = list(map(int,input().split()))

num_card=dict()
num=cards.pop()
num_card[num] = 1
pnum = num

for i in range(len(cards)):
    num=cards.pop()
    if num == pnum:
        num_card[num] +=1
    else:
        num_card[num] = 1
    pnum=num

for x in count_card:
    print(num_card.get(x) if num_card.get(x) != None else 0, end=' ')