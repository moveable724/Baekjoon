n =int(input())
death_list = []

i = 0


while len(death_list) < n:
    i+=1
    if str(i).count('666') >= 1:
        death_list.append(i)
    
print(death_list[-1])    
       