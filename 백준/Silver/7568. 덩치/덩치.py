n =int(input())
size_list=[]
for __ in range(n):
    size_list.append(list(map(int, input().split())))
    
for target in size_list:
    n=1
    for i in size_list:
        if target[0] < i[0] and target[1] < i[1]:
            n+=1
    print(n, end=' ')        