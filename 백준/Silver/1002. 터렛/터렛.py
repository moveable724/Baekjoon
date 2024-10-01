import sys
input=sys.stdin.readline
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    if (x1, y1) == (x2, y2):
        if r1 == r2:
            print(-1)  
        else:
            print(0)  
    else:
        d = (x1 - x2) ** 2 + (y1 - y2) ** 2  
        r_sum = (r1 + r2) ** 2  
        r_diff = (r1 - r2) ** 2  
        
        if r_diff < d < r_sum:
            print(2)  
        elif d == r_sum or d == r_diff:
            print(1)  
        else:
            print(0)