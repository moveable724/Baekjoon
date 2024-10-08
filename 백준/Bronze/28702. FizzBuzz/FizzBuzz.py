lst=[]
for i in range(3):
    n=(input())
    try:
        lst.append([int(n),i])
    except: pass
tnum=lst[0][0]+3-lst[0][1]
if tnum%3==0:
    if tnum%5==0:
        print('FizzBuzz')
    else:
        print('Fizz')
elif tnum%5==0:
    print('Buzz')
else:print(tnum)