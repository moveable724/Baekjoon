a,b,c = map(int,input().split())
res = 1
while b:
    if b % 2 ==1:
        res = res*a %c
    a = a*a % c
    b //=2
    
print(res)