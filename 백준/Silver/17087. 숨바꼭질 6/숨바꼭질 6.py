import sys
import math
input = sys.stdin.readline

n,s = map(int,input().split())
lst = list(map(int,input().split()))
lst2=[]
for i in lst:
    lst2.append(abs(i-s))
GCD = lst2[0]
for x in lst2:
    GCD = math.gcd(GCD, x)
    
print(GCD)