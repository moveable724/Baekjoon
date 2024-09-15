import math
import sys
num = int(sys.stdin.readline())
d = [0] * 100001
d[1] = 1

for i in range(2,num+1):
    d[i] = d[i-1] + 1
    for x in range(2, int(math.sqrt(i)) +1):
        d[i] = min(d[i], d[i- x**2] +1)

print(d[num])