from itertools import combinations
mo = 'aeiou'
m,n = map(int, input().split())
sum=0
lst  = list(map(str,input().split()))
lst2 = list(combinations(lst,m))
lst3 =[]
for i in lst2:
    c=0
    for x in range(5):
        if mo[x] in i:
            c+=1
    if c >=1:
        if m-c>=2:
            lst3.append(sorted(list(i)))

lst3.sort()
for i in lst3:
    print(''.join(i))