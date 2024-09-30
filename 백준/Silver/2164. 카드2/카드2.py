n=int(input())
num=0
while n>2**num:
    num+=1
print(int((n-2**(num-1))*2))
