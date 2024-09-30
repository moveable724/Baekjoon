n=int(input())
num=1
if n ==1:
    print(1)
else:
    while n> num:
        num*=2
    num//=2
    print(2*(n-num))