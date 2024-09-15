n=int(input())
for x in range(n):
    a,b=map(int,input().split())
    m=abs(a-b)
    i=2
    x=1
    num=0
    if m<=3:
        print(m)
    else:
        while m>num:
            if x ==1:
               num=i**2
               x*=-1
               i+=1
            else:
               num= i**2 -i
               x*=-1
        i-=1
        if x==-1:
            print(2*i-1)
        else:
            print(2*i)
