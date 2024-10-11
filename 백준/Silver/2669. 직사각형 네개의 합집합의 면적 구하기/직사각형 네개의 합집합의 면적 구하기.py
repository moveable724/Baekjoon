lst=[[0 for i in range(100)]for i in range(100)]
for i in range(4):
    x1,y1,x2,y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1,x2):
            if lst[x][y] == 0:
                lst[x][y]=1
    
ct=0            
for l in lst:
    ct+=l.count(1)
    
print(ct)