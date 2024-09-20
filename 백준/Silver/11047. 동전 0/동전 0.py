n,k = map(int,input().split())
lst=[]
for __ in range(n):
    lst.append(int(input()))
ct=0
i=1
while k !=0:
    if k>= lst[-i]:
        ct+=k//lst[-i]
        k=k%lst[-i]
    else:
        i+=1
        
print(ct)