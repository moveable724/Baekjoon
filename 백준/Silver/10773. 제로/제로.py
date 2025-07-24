import sys
input = sys.stdin.readline
n=int(input())
stack=[]
for i in range(n):
    num=int(input())
    stack.append(num) if num !=0 else stack.pop()
    
print(sum(stack))