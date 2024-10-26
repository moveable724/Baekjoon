import re

pattern = re.compile(r'^(100+1+|01)+$')
n = int(input())
for i in range(n):
    s = input().strip()
    if pattern.match(s):
        print('YES')
    else:
        print('NO')
