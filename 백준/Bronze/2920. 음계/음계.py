p = print
l = list(map(int,input().split()))
if l == sorted(l):
    p('ascending')
elif l == sorted(l, reverse=True):
    p('descending')
else:
    p('mixed')