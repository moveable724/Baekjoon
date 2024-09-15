from itertools import combinations

lst=list
while lst[0]!=0:
    lst= list(map(int,input().split()))
    if lst[0]==0:
        break
    n=lst[0]
    lst.pop(0)
    lst2= list(combinations(lst,6))
    for x in lst2:
        print(' '.join(map(str,x)))
    print()