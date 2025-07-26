import sys
input=sys.stdin.readline
n=int(input())
lst=list(map(int,input().split()))
m=int(input())
target_list = list(map(int,input().split()))
dic=dict()
for i in lst:
    dic[i]=1

for x in target_list:
    print(int(x in dic))