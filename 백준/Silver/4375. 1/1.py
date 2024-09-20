import sys
lst=sys.stdin.readlines()

for i in lst:
    num=int(i)
    target = 1
    while target%num != 0:
        target=target*10 + 1
    print(len(str(target)))