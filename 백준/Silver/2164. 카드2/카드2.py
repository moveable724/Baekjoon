from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
lst=deque([n for n in range(n,0,-1)])
while True:
    if len(lst) == 1:
        print(lst.pop())
        break
    lst.pop()
    lst.appendleft(lst.pop())