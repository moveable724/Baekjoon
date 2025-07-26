
import sys
input = sys.stdin.readline
n=int(input())
lst=[]
num_list=[0]*8001
for i in range(n):
    num=int(input())
    lst.append(num)
    num_list[num+4000]+=1

    
lst.sort()
x="{:.0f}".format(sum(lst)/n)
print(x) if x != '-0' else print(0)
print(lst[(n+1)//2-1])
max_val= max(num_list)
max_num = num_list.index(max(num_list)) - 4000
index=0
for i in range(-4000,4000):
        if num_list[i+4000] == max_val:
            index+=1
            max_num = i
        if index == 2:
            break
print(max_num)
print(max(lst) - min(lst))