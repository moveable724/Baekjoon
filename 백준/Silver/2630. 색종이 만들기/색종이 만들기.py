##2630
import sys
input = sys.stdin.readline

n = int(input()) # size of the square (nxn)
lst = [list(map(int, input().split())) for __ in range(n)]

w,b=0,0

def dividin_square(lst: list, loc: list , size: int) -> None:
    global w,b
    SUM = 0
    for i in range(loc[1], loc[1]+size):
        SUM+=sum(lst[i][loc[0]: loc[0]+size])
    if SUM==0:
        w+=1
        return
    elif SUM == size**2:
        b+=1
        return
    else:
        size = size // 2
        dividin_square(lst,loc,size)
        dividin_square(lst, [loc[0]+size, loc[1]], size)
        dividin_square(lst, [loc[0], loc[1]+size], size)
        dividin_square(lst, [loc[0]+size, loc[1]+size], size)        
    return


dividin_square(lst,[0,0],n)
print(w)
print(b)
