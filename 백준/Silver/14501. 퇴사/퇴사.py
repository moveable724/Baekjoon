n=int(input())
ts=[]

for __ in range(n):
    ts.append(list(map(int,input().split())))
    
for i in range(n):
    temp=[0]
    
    if ts[i][0]+ i > n:
        ts[i][1]=0
        continue
    
    for j in range(i):
        if ts[j][0] + j < i+1:
            temp.append(ts[j][1])
    ts[i][1]+=max(temp)
    
new=[]
for j in ts:
    new.append(j[1])

print(max(new))