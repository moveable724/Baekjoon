num = '0123456789'
alphabet = 'abcdefghijklmnopqrsrtuvwxyz'
Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while True:
    try:
        n = 0
        a = 0
        A = 0
        s = 0
        strin = input()
        if strin:
            lst = list(strin)
            for i in lst:
                if i == ' ':
                    s+=1
                elif i in num:
                    n+=1
                elif i in alphabet:
                    a +=1
                else: A+=1
            print(a,A,n,s)            
    except:
        break  