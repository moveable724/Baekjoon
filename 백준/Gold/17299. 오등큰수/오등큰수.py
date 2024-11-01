import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
count = Counter(lst)
answer = [-1] * n
stack = []

for i in range(n):
    while stack and count.get(lst[stack[-1]]) < count.get(lst[i]):
        answer[stack.pop()] = lst[i] 
    stack.append(i)  

print(*answer) 